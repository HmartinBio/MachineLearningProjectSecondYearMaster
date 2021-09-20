---
title: README
author: Hugo MARTIN
date: 09/01/2021
---

## Contents

[Overview of the Project](#overview-of-the-project)\
[Describing the Workspace](#describing-the-workspace)\
[Using Conda Environment](#using-conda-environment)\
[Launching Analysis](#launching-analysis)\
[GitLab Link](#gitlab-link)

## Overview of the Project

The goal of the project was to study the efficiency of the neural network model to predict types of cancers\
from the **Cancer Genome Atlas Dataset** (see [report](report/Designing-a-Machine-learning-strategy-to-predict-types-of-cancers.pdf)).

## Prerequites

This project was designed on a **Linux** system, it is recommended to be on this **Operating System** to execute scripts.\
**Figures** and **output files** can be read on all **Operating Systems**, but if you want execute scripts to make analysis,\
it is better to be on a **Linux** system. 

The execution of scripts need to activate the **Conda Environment**.\
All the analysis were **launched** and all the **figures** were produced, so it is not necessary to launch **analysis** to generate and read **figures**.

Due to troubles to send data on GitHub, folders **data** and **output** were zipped, please **unzip** before to launch the project.

## Describing the Workspace

## [Conda_environment/](Conda_environment)
- [BiostatCondaEnv.yml](Conda_environment/BiostatCondaEnv.yml)

## [README.html](README.html)

## [README.md](README.md)

## [data/](data)
- [data.csv](data/data.csv)
- [labels.csv](data/labels.csv)

## [deleteAllOutput.sh](deleteAllOutput.sh)

## [figures/](figures)
- [AccuracyCurveWith3Layers100Epochs.eps](figures/AccuracyCurveWith3Layers100Epochs.eps)
- [AccuracyCurveWith3Layers100EpochsL1Equal0.01.eps](figures/AccuracyCurveWith3Layers100EpochsL1Equal0.01.eps)
- [AccuracyCurveWith3Layers100EpochsL1Equal0.1.eps](figures/AccuracyCurveWith3Layers100EpochsL1Equal0.1.eps)
- [AccuracyCurveWith3Layers20EpochsL1Equal0.01.eps](figures/AccuracyCurveWith3Layers20EpochsL1Equal0.01.eps)
- [AccuracyCurveWith3Layers20EpochsL1equal0.1.eps](figures/AccuracyCurveWith3Layers20EpochsL1equal0.1.eps)
- [AccuracyCurveWith3Layers2OEpochs.eps](figures/AccuracyCurveWith3Layers2OEpochs.eps)
- [AccuracyCurveWith3Layers50Epochs.eps](figures/AccuracyCurveWith3Layers50Epochs.eps)
- [AccuracyCurveWith3Layers50EpochsL1Equal0.01.eps](figures/AccuracyCurveWith3Layers50EpochsL1Equal0.01.eps)
- [AccuracyCurveWith3Layers50EpochsL1Equal0.1.eps](figures/AccuracyCurveWith3Layers50EpochsL1Equal0.1.eps)
- [AccuracyCurveWith4Layers100Epochs4Layers.eps](figures/AccuracyCurveWith4Layers100Epochs4Layers.eps)
- [AccuracyCurveWith4Layers100EpochsL1Equal0.01.eps](figures/AccuracyCurveWith4Layers100EpochsL1Equal0.01.eps)
- [AccuracyCurveWith4Layers100EpochsL1Equal0.1.eps](figures/AccuracyCurveWith4Layers100EpochsL1Equal0.1.eps)
- [AccuracyCurveWith4Layers20Epochs4Layers.eps](figures/AccuracyCurveWith4Layers20Epochs4Layers.eps)
- [AccuracyCurveWith4Layers20EpochsAndL1Equal0.01.eps](figures/AccuracyCurveWith4Layers20EpochsAndL1Equal0.01.eps)
- [AccuracyCurveWith4Layers20EpochsAndL1Equal0.1.eps](figures/AccuracyCurveWith4Layers20EpochsAndL1Equal0.1.eps)
- [AccuracyCurveWith4Layers50Epochs4Layers.eps](figures/AccuracyCurveWith4Layers50Epochs4Layers.eps)
- [AccuracyCurveWith4Layers50EpochsL1Equal0.01.eps](figures/AccuracyCurveWith4Layers50EpochsL1Equal0.01.eps)
- [AccuracyCurveWith4Layers50EpochsL1Equal0.1.eps](figures/AccuracyCurveWith4Layers50EpochsL1Equal0.1.eps)
- [BestNeuralNetworkAccuracyPlot.eps](figures/BestNeuralNetworkAccuracyPlot.eps)
- [BestNeuralNetworkLossCurve.eps](figures/BestNeuralNetworkLossCurve.eps)
- [LearningCurveWithFourLayers.eps](figures/LearningCurveWithFourLayers.eps)
- [LearningCurveWithFourLayersAndL1Equal0.01.eps](figures/LearningCurveWithFourLayersAndL1Equal0.01.eps)
- [LearningCurveWithFourLayersAndL1Equal0.1.eps](figures/LearningCurveWithFourLayersAndL1Equal0.1.eps)
- [LearningCurveWithThreeLayers.eps](figures/LearningCurveWithThreeLayers.eps)
- [LearningCurveWithThreeLayersAndL1Equal0.01.eps](figures/LearningCurveWithThreeLayersAndL1Equal0.01.eps)
- [LearningCurveWithThreeLayersAndL1Equal0.1.eps](figures/LearningCurveWithThreeLayersAndL1Equal0.1.eps)
- [PCAFigure.eps](figures/PCAFigure.eps)
- [SupplementaryData.docx](figures/SupplementaryData.docx)
- [SupplementaryData.pdf](figures/SupplementaryData.pdf)
- [UMAPFigure.eps](figures/UMAPFigure.eps)

## [lib/](lib)
- [AssamblingData.py](lib/AssamblingData.py)
- [NeuronalNetworkOnSubsetOfData.py](lib/NeuronalNetworkOnSubsetOfData.py)
- [PCAVisualisation.py](lib/PCAVisualisation.py)
- [SimpleNeuronalNetwork.py](lib/SimpleNeuronalNetwork.py)
- [UMAPVisualisation.py](lib/UMAPVisualisation.py)
- [VarianceGenes.R](lib/VarianceGenes.R)

## [main.py](main.py)

## [output/](output)
- [2264GenesDataframe/](output/2264GenesDataframe)
  - [newDataFrame.csv](output/2264GenesDataframe/newDataFrame.csv)
- [399GenesDataframe/](output/399GenesDataframe)
  - [newDataFrame.csv](output/399GenesDataframe/newDataFrame.csv)
- [CompleteData.csv](output/CompleteData.csv)

## [report/](report)
- [Designing-a-Machine-learning-strategy-to-predict-types-of-cancers.pdf](report/Designing-a-Machine-learning-strategy-to-predict-types-of-cancers.pdf)
-----


**Conda_environment** contains the **Conda Environment** used to execute some codes.\
**data** is the folder containing all the input data to generate **output**.\
**ouput** is the folder containing all the output data.\
**figures** is the folder containing all the figures generated from **output**.\
**report** is the folder containing the report.\
**lib** is the folder containing all the codes used to generate output data.\
**figures/SupplementaryData.pdf** contains all the **figures** generated during the study.

<br>

## Using Conda Environment

<br>

### Installing Conda

If you didn't install **Conda** on your computer, you can follow this [link](https://docs.conda.io/en/latest/miniconda.html) to install it.

<br>

### Deploying the Conda Environment on your computer

To deploy the **Conda** environment on your computer, go to the **Conda_environment** folder. Then, use the command:


```{bash}
conda env create -f BiostatCondaEnv.yml
```

To deploy the environment.

<br>

### Activating the Conda Environment

To use the **Conda** environment on your computer, you must entry the command:

```{bash}
conda activate Biostat
```
<br>

### MiniConda Environment Content

The used **Conda** packages for this project are listed below.

name: Biostat\

channels:

  - conda-forge
  - bioconda
  - defaults
  - r

dependencies:

  - _libgcc_mutex=0.1=conda_forge
  - _openmp_mutex=4.5=1_gnu
  - _py-xgboost-mutex=2.0=cpu_0
  - _r-mutex=1.0.1=anacondar_1
  - absl-py=0.11.0=py36h5fab9bb_0
  - astor=0.8.1=pyh9f0ad1d_0
  - binutils_impl_linux-64=2.35.1=h193b22a_1
  - binutils_linux-64=2.35=hc3fd857_29
  - bwidget=1.9.14=ha770c72_0
  - bzip2=1.0.8=h7f98852_4
  - c-ares=1.17.1=h36c2ea0_0
  - ca-certificates=2020.12.5=ha878542_0
  - cached-property=1.5.1=py_0
  - cairo=1.16.0=h9f066cc_1006
  - certifi=2020.12.5=py36h5fab9bb_0
  - curl=7.71.1=he644dc0_8
  - cycler=0.10.0=py_2
  - dbus=1.13.6=hfdff14a_1
  - expat=2.2.9=he1b5a44_2
  - fontconfig=2.13.1=h7e3eb15_1002
  - freetype=2.10.4=h7ca028e_0
  - fribidi=1.0.10=h36c2ea0_0
  - gast=0.4.0=pyh9f0ad1d_0
  - gcc_impl_linux-64=9.3.0=h28f5a38_17
  - gcc_linux-64=9.3.0=h7247604_29
  - gettext=0.19.8.1=h0b5b191_1005
  - gfortran_impl_linux-64=9.3.0=h2bb4189_17
  - gfortran_linux-64=9.3.0=ha1c937c_29
  - glib=2.66.4=hcd2ae1e_1
  - google-pasta=0.2.0=pyh8c360ce_0
  - graphite2=1.3.13=h58526e2_1001
  - grpcio=1.34.0=py36h8e87921_0
  - gsl=2.6=he838d99_1
  - gst-plugins-base=1.14.5=h0935bb2_2
  - gstreamer=1.18.2=h3560a44_1
  - gxx_impl_linux-64=9.3.0=h53cdd4c_17
  - gxx_linux-64=9.3.0=h0d07fa4_29
  - h5py=3.1.0=nompi_py36hc1bc4f5_100
  - harfbuzz=2.7.2=ha5b49bf_1
  - hdf5=1.10.6=nompi_h6a2412b_1113
  - icu=67.1=he1b5a44_0
  - importlib-metadata=3.3.0=py36h5fab9bb_2
  - joblib=1.0.0=pyhd8ed1ab_0
  - jpeg=9d=h36c2ea0_0
  - keras=2.3.1=py36_0
  - keras-applications=1.0.8=py_1
  - keras-preprocessing=1.1.0=py_0
  - kernel-headers_linux-64=2.6.32=h77966d4_13
  - kiwisolver=1.3.1=py36h51d7077_0
  - krb5=1.17.2=h926e7f8_0
  - lcms2=2.11=hcbb858e_1
  - ld_impl_linux-64=2.35.1=hea4e1c9_1
  - libblas=3.9.0=6_openblas
  - libcblas=3.9.0=6_openblas
  - libclang=11.0.0=default_ha5c780c_2
  - libcurl=7.71.1=hcdd3856_8
  - libedit=3.1.20191231=he28a2e2_2
  - libev=4.33=h516909a_1
  - libevent=2.1.10=hcdb4288_3
  - libffi=3.3=h58526e2_2
  - libgcc-devel_linux-64=9.3.0=hfd08b2a_17
  - libgcc-ng=9.3.0=h5dbcf3e_17
  - libgfortran-ng=9.3.0=he4bcb1c_17
  - libgfortran5=9.3.0=he4bcb1c_17
  - libglib=2.66.4=h164308a_1
  - libgomp=9.3.0=h5dbcf3e_17
  - libgpuarray=0.7.6=h14c3975_1003
  - libiconv=1.16=h516909a_0
  - liblapack=3.9.0=6_openblas
  - libllvm10=10.0.1=he513fc3_3
  - libllvm11=11.0.0=he513fc3_0
  - libnghttp2=1.41.0=h8cfc5f6_2
  - libopenblas=0.3.12=pthreads_h4812303_1
  - libpng=1.6.37=h21135ba_2
  - libpq=12.3=h255efa7_3
  - libprotobuf=3.14.0=h780b84a_0
  - libssh2=1.9.0=hab1572f_5
  - libstdcxx-devel_linux-64=9.3.0=h4084dd6_17
  - libstdcxx-ng=9.3.0=h2ae2ef3_17
  - libtiff=4.2.0=hdc55705_0
  - libuuid=2.32.1=h7f98852_1000
  - libwebp-base=1.1.0=h36c2ea0_3
  - libxcb=1.13=h14c3975_1002
  - libxgboost=1.3.0=h9c3ff4c_1
  - libxkbcommon=1.0.3=he3ba5ed_0
  - libxml2=2.9.10=h68273f3_2
  - llvmlite=0.35.0=py36h05121d2_0
  - lz4-c=1.9.3=h9c3ff4c_0
  - make=4.3=hd18ef5c_1
  - mako=1.1.3=pyh9f0ad1d_0
  - markdown=3.3.3=pyh9f0ad1d_0
  - markupsafe=1.1.1=py36he6145b8_2
  - matplotlib=3.3.3=py36h5fab9bb_0
  - matplotlib-base=3.3.3=py36he12231b_0
  - mysql-common=8.0.22=ha770c72_1
  - mysql-libs=8.0.22=h1fd7589_1
  - ncurses=6.2=h58526e2_4
  - nspr=4.29=he1b5a44_1
  - nss=3.60=hb5efdd6_0
  - numba=0.52.0=py36h284efc9_0
  - numpy=1.19.4=py36h2aa4a07_2
  - olefile=0.46=pyh9f0ad1d_1
  - openssl=1.1.1i=h7f98852_0
  - pandas=1.1.5=py36h284efc9_0
  - pandoc=2.11.3.2=h7f98852_0
  - pango=1.42.4=h69149e4_5
  - pcre=8.44=he1b5a44_0
  - pcre2=10.36=h032f7d1_0
  - pillow=8.1.0=py36h4f9996e_0
  - pip=20.3.3=pyhd8ed1ab_0
  - pixman=0.40.0=h36c2ea0_0
  - protobuf=3.14.0=py36hc4f0c31_0
  - pthread-stubs=0.4=h36c2ea0_1001
  - py-xgboost=1.3.0=py36h5fab9bb_1
  - pygpu=0.7.6=py36h68bb277_1002
  - pyparsing=2.4.7=pyh9f0ad1d_0
  - pyqt=5.12.3=py36h5fab9bb_6
  - pyqt-impl=5.12.3=py36h7ec31b9_6
  - pyqt5-sip=4.19.18=py36hc4f0c31_6
  - pyqtchart=5.12=py36h7ec31b9_6
  - pyqtwebengine=5.12.1=py36h7ec31b9_6
  - python=3.6.12=hffdb5ce_0_cpython
  - python-dateutil=2.8.1=py_0
  - python_abi=3.6=1_cp36m
  - pytz=2020.5=pyhd8ed1ab_0
  - pyyaml=5.3.1=py36he6145b8_1
  - qt=5.12.9=h763d07f_1
  - r-base=4.0.3=ha43b4e8_3
  - r-base64enc=0.1_3=r40hcdcec82_1004
  - r-digest=0.6.27=r40h1b71b39_0
  - r-evaluate=0.14=r40h6115d3f_2
  - r-glue=1.4.2=r40hcdcec82_0
  - r-highr=0.8=r40h6115d3f_2
  - r-htmltools=0.5.0=r40h0357c0b_0
  - r-jsonlite=1.7.2=r40hcfec24a_0
  - r-knitr=1.30=r40h6115d3f_0
  - r-lattice=0.20_41=r40hcdcec82_2
  - r-magrittr=2.0.1=r40h9e2df91_1
  - r-markdown=1.1=r40hcdcec82_1
  - r-matrix=1.3_0=r40he454529_0
  - r-mime=0.9=r40hcdcec82_1
  - r-rappdirs=0.3.1=r40hcdcec82_1004
  - r-rcpp=1.0.5=r40he524a50_0
  - r-reticulate=1.18=r40h1b71b39_0
  - r-rlang=0.4.10=r40hcfec24a_0
  - r-rmarkdown=2.6=r40hc72bb7e_0
  - r-stringi=1.5.3=r40h604b29c_0
  - r-stringr=1.4.0=r40h6115d3f_2
  - r-tinytex=0.28=r40hc72bb7e_0
  - r-xfun=0.19=r40h9e2df91_0
  - r-yaml=2.2.1=r40hcdcec82_1
  - readline=8.0=he28a2e2_2
  - scikit-learn=0.24.0=py36he4fde30_0
  - scipy=1.5.3=py36h9e8f40b_0
  - sed=4.8=he412f7d_0
  - setuptools=49.6.0=py36h9880bd3_2
  - six=1.15.0=pyh9f0ad1d_0
  - sqlite=3.34.0=h74cdb3f_0
  - sysroot_linux-64=2.12=h77966d4_13
  - tbb=2020.2=h4bd325d_2
  - tensorboard=1.14.0=py36_0
  - tensorflow=1.14.0=hc3e5e64_0
  - tensorflow-base=1.14.0=py36hc3e5e64_0
  - tensorflow-estimator=1.14.0=py36h5ca1d4c_0
  - termcolor=1.1.0=py_2
  - theano=0.9.0=py36_1
  - threadpoolctl=2.1.0=pyh5ca1d4c_0
  - tk=8.6.10=h21135ba_1
  - tktable=2.10=hb7b940f_3
  - tornado=6.1=py36h1d69622_0
  - typing_extensions=3.7.4.3=py_0
  - umap-learn=0.4.6=py36h9f0ad1d_0
  - werkzeug=1.0.1=pyh9f0ad1d_0
  - wheel=0.36.2=pyhd3deb0d_0
  - wrapt=1.12.1=py36h1d69622_2
  - xgboost=1.3.0=py36hc4f0c31_1
  - xorg-kbproto=1.0.7=h14c3975_1002
  - xorg-libice=1.0.10=h516909a_0
  - xorg-libsm=1.2.3=h84519dc_1000
  - xorg-libx11=1.6.12=h516909a_0
  - xorg-libxau=1.0.9=h14c3975_0
  - xorg-libxdmcp=1.1.3=h516909a_0
  - xorg-libxext=1.3.4=h516909a_0
  - xorg-libxrender=0.9.10=h516909a_1002
  - xorg-libxt=1.2.0=h516909a_0
  - xorg-renderproto=0.11.1=h14c3975_1002
  - xorg-xextproto=7.3.0=h14c3975_1002
  - xorg-xproto=7.0.31=h7f98852_1007
  - xz=5.2.5=h516909a_1
  - yaml=0.2.5=h516909a_0
  - zipp=3.4.0=py_0
  - zlib=1.2.11=h516909a_1010
  - zstd=1.4.8=ha95c52a_1

prefix: /home/hugo/miniconda3/envs/Biostat
<br>


## Launching Analysis

To generate all the output files and all the figures, you must execute the **main.py** python script.\
For that, you must go in the **root folder of the project** and execute this command after activating the **Conda Environement**:

```{python}
python3 main.py
```

To delete all the **figures** and the **output** files, you can execute the **deleteAllOutput.sh** bash script in the **root folder of the project**.\
For that, you must execute this command:

```{bash}
./deleteAllOutput.sh
```

## GitLab Link

This project is available on [GitLab](https://gitlab.com/bioraspi83/projet_de_biostatistiques_approfondies)
