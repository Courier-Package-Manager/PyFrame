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
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/GH-Syn/PyFrame">
    <img src=".github/Images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">PyFrame</h3>

  <p align="center">
    The modern framework for PyGame
    <br />
    <a href="https://github.com/GH-Syn/PyFrame"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/GH-Syn/PyFrame">View Demo</a>
    ·
    <a href="https://github.com/GH-Syn/PyFrame/issues">Report Bug</a>
    ·
    <a href="https://github.com/GH-Syn/PyFrame/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About PyFrame

I'll start off by explaining why this project has been created.

I found myself typing out the same shit every time I wanted to add something new to pygame, whether that be
physics, more sprites, assets, whatever. I eventually, as with everything, realized that I could, to an extent,
automate (kind of) the process. This repository is something that I myself plan to use in my projects. This project
*is* open source, however please credit this repository if it's used elsewhere.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get starteds, simply install install PyFrame and import it into your project.

### Prerequisites

Install pyframe with GitHub.

git clone https://github.com/GH-Syn/PyFrame.git

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

```python
import pyframe

player = pyframe.player(x=10, y=10)

tiles = [
    pyframe.tile2d(x=10, y=50, color=pyframe.red),
    pyframe.tile2d(x=50, y=100, width=50, height=50, color=pyframe.white)
]

voxel_tile = pyframe.tile3d(x=10, y=50, z=100)
```

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/GH-Syn/PyFrame.svg?style=for-the-badge
[contributors-url]: https://github.com/GH-Syn/PyFrame/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/GH-Syn/PyFrame.svg?style=for-the-badge
[forks-url]: https://github.com/GH-Syn/PyFrame/network/members
[stars-shield]: https://img.shields.io/github/stars/GH-Syn/PyFrame.svg?style=for-the-badge
[stars-url]: https://github.com/GH-Syn/PyFrame/stargazers
[issues-shield]: https://img.shields.io/github/issues/GH-Syn/PyFrame.svg?style=for-the-badge
[issues-url]: https://github.com/GH-Syn/PyFrame/issues
[license-shield]: https://img.shields.io/github/license/GH-Syn/PyFrame.svg?style=for-the-badge
[license-url]: https://github.com/GH-Syn/PyFrame/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
