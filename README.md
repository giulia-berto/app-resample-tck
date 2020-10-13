[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.124-blue.svg)](https://doi.org/10.25663/brainlife.app.124)

# app-resample-tck
This App resamples the streamlines of a tractogram (in tck format) with a given step size or, alternatively, with a given number of points.

### Authors
- Giulia Bertò (giulia.berto.4@gmail.com)

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

1. Tournier, J.‐D., Calamante, F. and Connelly, A. (2012), MRtrix: Diffusion tractography in crossing fiber regions. Int. J. Imaging Syst. Technol., 22: 53-66. [https://doi.org/10.1002/ima.22005](https://doi.org/10.1002/ima.22005)

2. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

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

### Output
The output file, called `track.tck`, is the resampled tractogram.

### Dependencies
This App requires [singularity](https://sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies. It also requires [jq](https://stedolan.github.io/jq/).

#### MIT Copyright (c) 2019 Giulia Bertò
