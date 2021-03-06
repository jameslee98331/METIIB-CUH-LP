# University of Cambridge MET IIB - Cambridge University Hospitals NHS Foundation Trust Long Project
## Summary

<div align="center">
<img src="https://github.com/jameslee98331/METIIB-CUH-LP/blob/master/README_images/overall_process.png" alt="The Biopsy Preparation Process" height="150">
</div>

Histopathology is the microscopic examination of a biopsy by a pathologist. A biopsy is a procedure that takes tissue from the body to make a diagnosis of medical conditions. The biopsy preparation process turns tissue from the body into histology slides. This process consists of 7 steps: collection, grossing, processing, embedding, microtomy, and staining, and examination. This project focuses on the automation of the embedding sub-process. The embedding process takes in processed tissues in cassettes and outputs tissues embedded in wax blocks.

<div align="center">
<img src="https://github.com/jameslee98331/METIIB-CUH-LP/blob/master/README_images/embed_process.png" alt="The Embedding Process" height="150">
</div>

The histopathology laboratory at Cambridge University Hospitals NHS Foundation Trust (CUH) currently experiences efficiency problems. The demand has risen by 9.40% and the FTE staff count has risen by 22.76% in the past 3 years. However, the KPI measurement for efficiency has dramatically decreased to 35-40%, half of the 80% target. The key causes for this decrease in efficiency are skills shortages and constraints with working hours. With the increasing demand for pathology services and expectations for high quality results, there is a need for automation in histopathology labs to improve efficiency.

This project analyses the current embedding process to understand how it may be automated. Decisions made by the technicians are highlighted and they must be replicated by the automation system. Literature on existing auto-embedding systems reveals that they do not eliminate the manual part of tissue orientation, which is a key step in the embedding process.

A concept design is proposed to address this technology gap by using robotics, computer vision, and machine learning. A functional specification is written, and detail designs are made for some of the functional components including the robotic arm, component fixtures, and feeders. A prototype for deep computer vision is also developed. The prototyped inference model classifies mock skin tissue images into skin or non-skin categories with a training accuracy of 99.2% and validation accuracy of 85%. The model is built from transfer learning from a pre-trained convolutional neural network.
The concept design and prototype show clear potential in automating the embedding process. This project forms the foundations for future developments. More research needs to be done to bring this forward into a financially viable and operationally deployable system.

Key Recommendations:
-	Continue to research into developing this system into a locally deployable state,
-	Expand on existing infrastructure, such as LIMS, image databases and NHS’ cloud computing resources, to enable a suitable development environment for the automation system,
-	Involve biomedical scientists and lab technicians in the development of the automation system to harness their expertise and knowledge while building harmony between the workforce and the machines, and
-	Consider automation while innovating new processes to prepare biopsies.

*Wang Kei James Lee* \
*Manufacturing Engineering Tripos Part IIB* \
*7th June 2020*

## Automation System Concept Design
### Overall System Flowchart
<div align="center">
<img src="https://github.com/jameslee98331/METIIB-CUH-LP/blob/master/README_images/work_flow.png" alt="System Work Flow" height="450">
</div>

### Information Flowchart
<div align="center">
<img src="https://github.com/jameslee98331/METIIB-CUH-LP/blob/master/README_images/system_design_deployment.png" alt="System Information Flow" height="250">
</div>

### Concept Sketch
System Layout |
:-------------------------:|
<img src="https://github.com/jameslee98331/METIIB-CUH-LP/blob/master/README_images/layout.png" alt="System Layout" height="300"> |

Robotic Arm | End Effector
:-------------------------:|:-------------------------:
<img src="https://github.com/jameslee98331/METIIB-CUH-LP/blob/master/README_images/robotic_arm.png" alt="Robotic Arm" height="300"> | <img src="https://github.com/jameslee98331/METIIB-CUH-LP/blob/master/README_images/end_effector.png" alt="End Effector" height="300">

Mould Feeder | Mould Fixture
:-------------------------:|:-------------------------:
<img src="https://github.com/jameslee98331/METIIB-CUH-LP/blob/master/README_images/mould_feeder.png" alt="Mould Feeder" height="350"> | <img src="https://github.com/jameslee98331/METIIB-CUH-LP/blob/master/README_images/mould_fixture.png" alt="Mould Fixture" height="200">

Cassette Fixture |
:-------------------------:|
<img src="https://github.com/jameslee98331/METIIB-CUH-LP/blob/master/README_images/cassette_fixture.png" alt="Cassette Fixture" height="300"> |

## Computer Vision Prototype
Skin Layer | Non-Skin Layer
:-------------------------:|:-------------------------:
<img src="https://github.com/jameslee98331/METIIB-CUH-LP/blob/master/README_images/skin.JPG" alt="Skin Layer" height="250"> | <img src="https://github.com/jameslee98331/METIIB-CUH-LP/blob/master/README_images/non_skin.JPG" alt="Non-Skin Layer" height="250">
