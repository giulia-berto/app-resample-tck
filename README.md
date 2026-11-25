<h1 align="center">Resample tck</h1>

<p align="center">
  Resamples the streamlines of a .tck tractogram to a new step size (mm) or a fixed number of points per streamline with DIPY.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.124"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.124-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Resamples the streamlines of a .tck tractogram to a new step size (mm) or a fixed number of points per streamline with DIPY.**

Loads the tractogram with nibabel and resamples each streamline with dipy set_number_of_points, either to floor(length/step) points for a given step size or to a fixed number of points, and saves a new .tck. Use it to harmonise streamline sampling before segmentation or comparison methods that expect a given step size or point count.

| | |
|---|---|
| **Inputs** | `neuro/track/tck` |
| **Outputs** | `neuro/track/tck` |
| **Container** | `brainlife/dipy:0.14` |
| **Resources** | 1 CPUs · 0.17 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.124](https://doi.org/10.25663/brainlife.app.124) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `0` | `neuro/track/tck` | yes | tractogram |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `tck` | `neuro/track/tck` | resampled tractogram |

<details>
<summary><b>Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `type` | enum |  | Resampling can be done either by setting the new step size (in mm) or the new number of points. Tell which option you want to use. Options: `step_size`, `nb_points`. |
| `new_param` | number |  | Set the step size OR the number of points, depending on your choice above |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.124](https://doi.org/10.25663/brainlife.app.124), choose `neuro/track/tck` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/track/tck`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/dipy:0.14`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "track": "/path/to/0/track",
       "type": "",
       "new_param": "<number>"
   }
   ```

3. Run `./main`.

## Troubleshooting

- **Resampling failed.**: Check that type and new_param are set and the input is a valid .tck file.

## On [Brainlife.io](http://brainlife.io/)

You can submit this App online at https://doi.org/10.25663/brainlife.app.124 via the “Execute” tab.

Input: \
A tractogram in tck format. Resampling can be done either by setting the new step size (in mm) or the new number of points. 

Output: \
The new resampled tractogram.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Resample tck. brainlife.io App. [doi:10.25663/brainlife.app.124](https://doi.org/10.25663/brainlife.app.124)
- Tournier J-D, Calamante F, Connelly A. MRtrix: Diffusion tractography in crossing fiber regions. Int J Imaging Syst Technol 22:53-66 (2012). [doi:10.1002/ima.22005](https://doi.org/10.1002/ima.22005)
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Giulia Bertò

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>
