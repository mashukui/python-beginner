<div align="center">

# Ma Ge's Python for Absolute Beginners

**7 lectures · 13 videos · ~78 minutes · Chinese narration**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-2ea44f?style=flat-square)
![Bilibili](https://img.shields.io/badge/Bilibili-13%20videos-00A1D6?style=flat-square&logo=bilibili&logoColor=white)

[中文 README](README.md) ｜ [📺 Videos](https://www.bilibili.com/video/BV1aK4y1F7g9) ｜ [🌐 Website](https://mgcoding.com)

</div>

---

> **Note:** The course is taught in Chinese. This English README is a summary for international visitors; the notebooks, PDFs and videos are all in Chinese.

## About

This is a short, practical Python course for people who have never written code. It was originally a paid private course, released for free on Bilibili in September 2023. The complete Jupyter notebooks and PDF handouts are now open-sourced.

The course focuses on the syntax you actually need as a beginner — no third-party libraries, no data-science detour, no "build ten projects" filler. Just 7 lectures that take you from installing Python to writing your first classes.

**What you will learn**

- What Python is, where it is used, and how to install it
- The six core types: numbers, strings, lists, tuples, dicts, sets — plus slicing, formatting and deduplication
- `if` statements, `for` / `while` loops, `break` / `continue`
- Functions: arguments, default values, keyword arguments, return values, `lambda`
- Classes, instances, inheritance, private attributes
- A foundation for moving on to pandas, web scraping, Flask/Django or automation

## Course outline

| # | Topic | Video | Length | Notebook |
| :--: | --- | :--: | ---: | :--: |
| 1 | Introduction to Python | [watch](https://www.bilibili.com/video/BV1aK4y1F7g9?p=1) | 6:36 | [ipynb](notebooks/第1讲-Python介绍.ipynb) · [PDF](pdf/第1讲-Python介绍.pdf) |
| 2 | Installing Python & PyCharm | [watch](https://www.bilibili.com/video/BV1aK4y1F7g9?p=2) | 4:02 | [ipynb](notebooks/第2讲-Python安装及PyCharm安装.ipynb) · [PDF](pdf/第2讲-Python安装及PyCharm安装.pdf) |
| 3 | Data types | [3.1–3.6](https://www.bilibili.com/video/BV1aK4y1F7g9?p=3) | 32:43 | [ipynb](notebooks/第3讲-Python数据类型.ipynb) · [PDF](pdf/第3讲-Python数据类型.pdf) |
| 4 | Conditionals | [watch](https://www.bilibili.com/video/BV1aK4y1F7g9?p=9) | 8:30 | [ipynb](notebooks/第4讲-Python条件判断.ipynb) · [PDF](pdf/第4讲-Python条件判断.pdf) |
| 5 | Loops | [5.1–5.2](https://www.bilibili.com/video/BV1aK4y1F7g9?p=10) | 11:11 | [ipynb](notebooks/第5讲-Python循环语句.ipynb) · [PDF](pdf/第5讲-Python循环语句.pdf) |
| 6 | Functions | [watch](https://www.bilibili.com/video/BV1aK4y1F7g9?p=12) | 6:03 | [ipynb](notebooks/第6讲-Python函数.ipynb) · [PDF](pdf/第6讲-Python函数.pdf) |
| 7 | Object-oriented programming | [watch](https://www.bilibili.com/video/BV1aK4y1F7g9?p=13) | 8:30 | [ipynb](notebooks/第7讲-Python面向对象.ipynb) · [PDF](pdf/第7讲-Python面向对象.pdf) |

Lecture 3 is split into six videos (numbers, strings, lists, tuples, dicts, sets); lecture 5 is split into two (for / while). The whole course is 13 videos in total.

## Companion website

The 7 lectures are a fast overview. For a slower, chapter-by-chapter path — including exceptions, file I/O and modules — I maintain a Chinese-language tutorial site: [马哥的python小屋](https://mgcoding.com) (7 chapters, 25 lessons, from Hello World to OOP).

The site is in Chinese; the notebooks and code in this repo remain language-agnostic.

## Run the notebooks

```bash
# clone or download this repository first
cd python-beginner/notebooks

python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install notebook
jupyter notebook
```

No third-party Python packages are required — every example uses the standard library only. The notebooks were recorded with Python 3.8.5; any Python 3.8+ interpreter works, and 3.10+ is recommended.

## Repository layout

```text
notebooks/   Jupyter notebooks + img/ (relative image assets)
pdf/         Printable PDF handouts for all 7 lectures
scripts/     build_pdf.py — regenerate the PDFs from the notebooks
```

## License

Text, code, notebooks, PDFs and images in this repository are released under the [MIT License](LICENSE).

The Bilibili videos are **not** covered by the MIT license. Their copyright belongs to the author; they are free to watch on Bilibili only.

Python is a trademark of the Python Software Foundation; PyCharm is a trademark of JetBrains. This course is not affiliated with either.
