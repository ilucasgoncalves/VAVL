# VAVL
Versatile Audio-Visual Learning for Handling Single and Multi Modalities in Emotion Regression and Classification Tasks. Learn 

## Abstract
A challenging task in audiovisual emotion recognition is to implement neural network architectures that can leverage and fuse multimodal information while temporally aligning modalities, handling missing modalities, and capturing information from all modalities without losing information during training. These requirements are important to achieve model robustness and to increase accuracy on the emotion recognition task. A recent approach to perform multimodal fusion is to use the transformer architecture to properly fuse and align the modalities. This study proposes the AuxFormer framework, which addresses in a principled way the aforementioned challenges. AuxFormer combines the transformer framework with auxiliary networks. It uses shared losses to infuse information from single-modality networks that are separately embedded. The extra layer of audiovisual information added to our main network retains information that would otherwise be lost during training.

### Paper
[Access to the paper](https://arxiv.org/pdf/2305.07216.pdf)
Lucas Goncalves, Seong-Gyun Leem, Wei-Cheng Lin, Berrak Sisman, and Carlos Busso "Versatile audiovisual learning for handling single and multi modalities in emotion regression and classification tasks," ArXiv e-prints (arXiv:2305.07216), pp. 1-14, May 2023.

Please cite our paper if you find our work useful for your research:

```tex
@article{Goncalves_2023_2,
	author = {L. Goncalves and S.-G. Leem and W.-C. Lin and B. Sisman and C. Busso},
	title = {Versatile Audiovisual Learning for Handling Single and Multi Modalities in Emotion Regression and Classification Tasks},
	journal = {ArXiv e-prints (arXiv:2305.07216 )},
	archivePrefix = {arXiv},
	eprint = {2305.07216 },
	primaryClass = {cs.LG},
	volume = {},
	number = {},
	year = {2023},
	pages = {1-14},
	month = {May},
	doi={10.48550/arXiv.2305.07216},
}
```

## Using model

### Dependencies
* Python 3.9.7
* Pytorch 1.12.1
* To create conda environment based on requirements use: `conda env create -f VAVL.yml`
* Activate environment with: `conda activate VAVL`

### Datasets Used
1. [CREMA-D](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4313618/) 
2. [MSP-IMPROV](https://ecs.utdallas.edu/research/researchlabs/msp-lab/MSP-Improv.html)

### Features & Partitions
*

