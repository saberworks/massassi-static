#!/usr/bin/perl

use warnings;
use strict;

use feature qw/say/;

use Cwd qw/getcwd/;
use Data::Dumper;

my $dir = '/home/brian/code/massassi/source/tutorials';
my $cwd = getcwd();

my @expected_indexes = qw/
    index.html
    index.htm
    index.shtml
    tutor.htm
/;

opendir my $dh, $dir or die "Can't open $dir: $!";

while(my $entry = readdir $dh) {
    next if $entry eq '.';
    next if $entry eq '..';
    next unless -d "$dir/$entry";

    my @files = glob("$dir/$entry/*.md");

    next if @files;

    die unless chdir "$dir/$entry";

    @files = glob("*.html *.htm *.shtml");

    my $index;

    foreach my $file (@files) {
        next if $file =~ /tutorial_print/;

        if(grep { $_ eq $file } @expected_indexes) {
            $index = $file;
        }
    }

    # if one of the expected index files is not present, but only a single htm, 
    # html, shtml file is present, consider that one the index
    if(!$index) {
        if(@files == 1) {
            $index = $files[0];
        }
    }

    if(!$index) {
        say "\tcould not find index for $entry";
        warn Dumper(\@files);
        next;
    }

    say "$entry: found index: $index";

    convert_html_to_markdown($entry, $index);

    chdir $cwd;
}

sub convert_html_to_markdown {
    my ($entry, $index) = @_;

    my $new_index = 'index.md';

    my $front = get_template($index);

    open(my $fh, '>', $new_index) or die "can't open $new_index: $!";
    print $fh $front;
    close $fh;

    my $exec = "pandoc --from html --to gfm $index >> $new_index";

    my $current_dir = getcwd();

    say "In $current_dir, going to execute:";
    say "\t$exec";

    `$exec`;
}

sub get_template {
    my $original = shift;

    my $template = qq{
---
title: 
author: 
email: 
description: >

date: 
original: $original
category: 
---

Author: 
    };

    $template =~ s/^\s*//;
    $template =~ s/\s*$//;

    return $template;
}
