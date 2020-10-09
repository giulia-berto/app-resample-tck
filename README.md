[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.124-blue.svg)](https://doi.org/10.25663/brainlife.app.124)

# app-resample-tck
This App resamples the streamlines of a tractogram (in tck format) with a given step size or, alternatively, with a given number of points.

### Authors
- Giulia Bertò (giulia.berto.4@gmail.com)

### Funding Acknowledgement
We kindly ask that you acknowledge the funding below in your publications and code reusing this code. \
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-AOC-1916518](https://img.shields.io/badge/NSF_AOC-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)

### Citation
We kindly ask that you cite the following article when publishing papers and code using this code. 

Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Running the app
### On [Brainlife.io](http://brainlife.io/) 
You can submit this App online at https://doi.org/10.25663/brainlife.app.124 via the “Execute” tab.

Input: \
A tractogram in tck format. Resampling can be done either by setting the new step size (in mm) or the new number of points. 

Output: \
The new resampled tractogram.

### Running locally
1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files:
```
{
    "track": "./track.tck",
    "type": "step_size",
    "new_param": 0.625
}
```
3. Launch the App by executing `main`.
```
./main
```

#### Dependencies
This App only requires [singularity](https://sylabs.io/singularity/) to run.

#### MIT Copyright (c) 2019 Giulia Bertò
