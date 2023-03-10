# -*- coding: utf-8 -*-
"""Word Document Automation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-cHOQpdefZx4oMr6L7UELQRvQYPh3QHT
"""

import pandas as pd
import numpy as np
import sys
import os
import docx
import image
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

gdp = pd.read_excel('Data.xlsx',sheet_name='GDP')
gdp.head()

template = DocxTemplate(r'Template.docx')
context = {
            'image1': InlineImage(template,r"data_science.jpeg",Cm(20)),
            'image2': InlineImage(template,r"data_science_requirement.jpeg",Cm(10)),
            'image3': InlineImage(template,r"data_scient_life_cycle.png",Cm(10)),
           
            'header_t1' : list(gdp),
            'data_t1'  : np.array(gdp),
           
            'paragraph1' : """ The combination of computer science, mathematics and business knowledge is critical to the success of data science projects. Without one of these elements, the data science process would be incomplete, and the insights generated would be less valuable. """,
            'paragraph2' : """ The data science lifecycle is a process that helps data scientists to structure their work and ensure that all important steps are covered. It typically includes several stages: problem definition, data acquisition, data preparation, data exploration, modeling, evaluation, deployment and monitoring.""",

            'para1': "Computer Science plays a crucial role in data science by providing the tools and techniques for collecting, storing, and manipulating large amounts of data. It also provides the algorithms and statistical models used in data analysis and machine learning. Knowledge of programming languages such as Python and R, as well as databases and big data technologies, is essential for a data scientist",
            'para2':"Mathematics is also a key component of data science. It provides the foundation for understanding the underlying statistical and probabilistic models used in data analysis. Knowledge of linear algebra, calculus, and optimization is necessary for understanding the mathematical concepts used in machine learning, such as gradient descent and neural networks.",
            'para3': "Business knowledge is important for data science because it provides context and relevance for the data analysis. A data scientist with a solid understanding of the business domain they are working in can better understand the problem they are trying to solve and how the insights they uncover can be used to drive business decisions. This can help to ensure that the data science project is aligned with the organization's goals and objectives.",
            'heading': "Insert words, table and image demo",
           
          }

template.render(context)
template.save(r'Output.docx')

os.system("start Output.docx")

