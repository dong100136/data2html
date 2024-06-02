from .element import DImage, DText
from .container import DTable
from typing import Dict, List
from collections.abc import Iterable
from string import Template
import os


class Theme:
    def render(self, view, data):
        out_html = self.render_table()

        path = os.path.join(os.path.dirname(__file__), "preview.html")
        with open(path) as f:
            html = "".join(f.readlines())
        template = Template(html)
        return template.substitute(data=out_html)

    def render_table(self):
        a = """
        <n-table :bordered="false" :single-line="false" size="small">
          <thead>
            <tr>
              <th>Abandon</th>
              <th>Abnormal</th>
              <th>Abolish</th>
              <th>...</th>
              <th>万事开头难</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>放弃</td>
              <td>反常的</td>
              <td>彻底废除</td>
              <td>...</td>
              <td>干！我刚才背的是啥</td>
            </tr>
            <tr>
              <td>...</td>
              <td>...</td>
              <td>...</td>
              <td>...</td>
              <td>...</td>
            </tr>
          </tbody>
        </n-table>
        """

        return a


class LightTheme(Theme):
    pass
