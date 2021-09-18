---
title: Character Model Import Tutorial - 6
---

Author: Michael Frost

## Skeletal Reference for Linking

**The Head and Facial Animation**

|  |            |                                                                        |
|  | ---------: | ---------------------------------------------------------------------- |
|  | Cervical - | Neck, blend between thoracic and cranium on both sides                 |
|  |  Cranium - | Weight to skull, if you don't want facial anims just weight whole head |
|  |      Jaw - | Link to the jaw and chin part of your model                            |
|  |   RtLip1 - | Inside top right lip                                                   |
|  |   RtLip2 - | Outside top right lip                                                  |
|  |   Rblip1 - | Inside bottom right lip                                                |
|  |   Rblip2 - | Outside bottom right lip                                               |
|  |   LtLip1 - | Inside top left lip                                                    |
|  |   LtLip2 - | Outside top left lip                                                   |
|  |   Lblip1 - | Inside bottom left lip                                                 |
|  |   Lblip2 - | Outside bottom left lip                                                |

**Tip:** Blend the center parts of the lower and upper lips with ltlip1
and rtlip1, and lblip1 and rblip1 for smooth animations on the face...
blend the corners of the mouth with the "2" bones.

|  |            |                                                     |
|  | ---------: | --------------------------------------------------- |
|  | Rbeyelid - | Bottom part of right eyelid, full weighting         |
|  | Rteyelid - | Top of right eyelid, full weighting                 |
|  | Lbeyelid - | Same as above, but for bottom left instead of right |
|  | Lteyelid - | Same as above but for top left instead of top right |

**Tip:** Don't weight the sides / corners of the eyes, just weight the
lids.

|  |             |                                               |
|  | ----------: | --------------------------------------------- |
|  | Reyebrow1 - | Inside of right eyebrow ridge                 |
|  | Reyebrow2 - | Outside of right eyebrow ridge                |
|  |  Ceyebrow - | Center of eyebrow ridge, above bridge of nose |
|  | Leyebrow2 - | Outside left eyebrow ridge                    |
|  | Leyebrow3 - | Inside left eyebrow ridge                     |

**Tip:** blend Reyebrow1 and 2, and 2 with Ceyebrow, then Ceyebrow with
Leyebrow2, then, Leyebrow2 with 3

|  |            |                                                                                |
|  | ---------: | ------------------------------------------------------------------------------ |
|  | Forehead - | Blend forehead into all eyebrow parts at bottom of forehead, then into cranium |
|  |    Cnose - | Not really necessary, weight nose to cranium                                   |

If you wish to cheat you can most likely skip a lot of the parts listed
and weight generally...

**Ways to Cheat:**

  - Leaving out 4 bones from the mouth (either all "2" bones or all "1"
    bones)
  - Leaving out the inner part of the eyebrows,
  - Simply leaving out the forehead bone completely

-----

**Body:**

|  |                |                                                                             |
|  | -------------: | --------------------------------------------------------------------------- |
|  |     Thoracic - | Collarbone area, blend with rclavical and lclavical, upper lumbar, cervical |
|  | Upper Lumbar - | Mid to upper rib cage, blend with lower lumbar and thoracic                 |
|  | Lower Lumbar - | Stomach, lower ribcage, into pelvis region, blend accordingly               |
|  |       Pelvis - | Hips bone area of model                                                     |

-----

**Right and Left of Torso:**

|  |             |                                                                   |
|  | ----------: | ----------------------------------------------------------------- |
|  | Rclavical - | Right side of upper torso, half of right shoulder                 |
|  |  Rhumerus - | Right shoulder, to mid-bicep                                      |
|  | RhumerusX - | Mid- bicep to mid-elbow                                           |
|  |   Rradius - | Mid-elbow to mid-forearm                                          |
|  |  RradiusX - | Mid-forearm to mid-wrist                                          |
|  |     Rhand - | Palm of hand, back of hand to knuckles, blend with thumb, fingers |
|  |       Mc7 - | Mix with Rhand, pinky finger                                      |
|  | R\_d1\_j1 - | Right thumb, first joint, blend into Rhand and R\_d1\_j2          |
|  | R\_d1\_j2 - | Right thumb, second joint, blend with first and third joint       |
|  | R\_d1\_j3 - | Right thumb, third joint, blend with second joint                 |

This pattern follows for the whole hand -- r\_dX\_jX, where d1 is thumb,
d2 is index finger, d3 is middle, d4 is ring finger, d5 is pinky, and
j1, j2 and j3 is which joint the bone is for.

Copy this exactly for the Left side parts of the model, but of course
mirrored\!

-----

**Legs**

|  |            |                                                                                 |
|  | ---------: | ------------------------------------------------------------------------------- |
|  | RfemurYZ - | Blend into pelvis bone at hip joint, not at crotch, blend at mid-thigh          |
|  |  RfemurX - | mid thigh, down to mid knee of model, blend with tibia and femurYZ              |
|  |   Rtibia - | Middle of knee joint, blend, whole shin, down to ankle, blend in middle of knee |
|  |   Rtalus - | heel, middle of foot, into toes, rigid setup at ankle and toes                  |
|  |  Rtarsal - | toes, fairly rigid bone setup                                                   |

Mirror for left leg.

**Note: About Extra Parts, Armor, Capes, etc.**

For linking these items to the bones, since Jedi Knight 2 currently does
not allow adding new skeletal mods and such, the cape, hair, clothing,
whatever must be linked to the body itself through the skeleton, meaning
those parts will simply deform along with the other parts. For example,
say you link the lower cape to the femur and tibia bones, that part of
the cape will animate with the femur and tibia bones, same as the legs.
Limitation, yes... hindrance, no.

As for more rigid items, you can simply bind them to a single bone,
instead of multiple bones, to give it a more solid look. Example: Exar
Kun's shoulder armor plates. They rest on each shoulder, and are only
bound to one upper arm bone.



* Back: [Setting Up a Skeleton](../5_SkeletalSetup/)
* [Return to this Tutorial's Table of Contents](../)
* Next: [Testing and Exporting Your Model as XSI](../7_ExportingFromMax/)
