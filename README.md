<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />

<h3 align="center">Expression Evaluation Post Pro</h3>

  <p align="center">
    a cura post processing script for evaluating arithmetic and logical expressions in g-code
    <br />
    <br />
    <a href="https://github.com/MrBraindead/CuraExpressionEvaluationPostPro/issues">Report Bug</a>
    ·
    <a href="https://github.com/MrBraindead/CuraExpressionEvaluationPostPro/issues">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This post-processing script allows you to perform math and logic operations in the start and end G-Code. 
Unlike Slic3r, Cura doesn't support this feature out of the box. With this script, you can evaluate arithmetic and logical expressions, giving you more control over your G-Code and making your workflow smoother.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Cura version 3.1.0 or newer

### Adding Script to Cura

1. In Cura go to ```Help > Show Configuraiton Folder```
2. In the Configuration Folder open the ```scipts``` folder and paste the [ArithmLogicExprEval.py](https://github.com/MrBraindead/CuraExpressionEvaluationPostPro/blob/main/ArithmLogicExprEval.py) script
3. Restart Cura

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

1. Click on the Post-Processing button ```</>``` next to the ```Slice``` Button.
2. Click ```Add a script```
3. Choose ```Arithmetic and Logical Expression Evaluation```

Expressions can be defined in start- and end- G-code as well as in other post-processing scripts.
When defining expressions in post processing scripts make sure those scripts are executed before this script.

Expressions must be in Python syntax. You can use any arithmetic and logical operators as well as parentheses and decimal points.

For example this start G-code draws a puge line at the Initial Layer Speed. ```{speed_layer_0}``` returns the Initial Layer Speed in mm/s. Therefore the expression gives the Initial Layer Speed in mm/min

```
G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position
G1 X0.1 Y200.0 Z0.3 F{speed_layer_0}*60 E15 ; Draw the first line
G1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little
G1 X0.4 Y20 Z0.3 F{speed_layer_0}*60 E30 ; Draw the second line
```
By default expressions in comments are ignored. You can tick the ```Evaluate Comments``` checkbox to evaluate expresions in comments.

The result of boolean expressions is represented as binary as this is the typical boolean representation in gcode. You can change the ```Boolean Representation``` to text in the options. 
This doesn't affect the boolean representaion in the expressions. Remeber that python uses text boolean representation (```True``` ```False```).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GNU LGPL v2.1 License. See [LICENSE](https://github.com/MrBraindead/CuraExpressionEvaluationPostPro/blob/main/LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/MrBraindead/CuraExpressionEvaluationPostPro.svg?style=for-the-badge
[contributors-url]: https://github.com/MrBraindead/CuraExpressionEvaluationPostPro/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/MrBraindead/CuraExpressionEvaluationPostPro.svg?style=for-the-badge
[forks-url]: https://github.com/MrBraindead/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/MrBraindead/CuraExpressionEvaluationPostPro.svg?style=for-the-badge
[stars-url]: https://github.com/MrBraindead/CuraExpressionEvaluationPostPro/stargazers
[issues-shield]: https://img.shields.io/github/issues/MrBraindead/CuraExpressionEvaluationPostPro.svg?style=for-the-badge
[issues-url]: https://github.com/MrBraindead/CuraExpressionEvaluationPostPro/issues
[license-shield]: https://img.shields.io/github/license/MrBraindead/CuraExpressionEvaluationPostPro.svg?style=for-the-badge
[license-url]: https://github.com/MrBraindead/CuraExpressionEvaluationPostPro/blob/master/LICENSE.txt
