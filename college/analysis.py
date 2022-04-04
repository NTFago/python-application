import pandas as pd # 导入 pandas 库 用于导入数据
import numpy as np
from pyecharts.charts import Bar, Page, Map, Line  # 导入 pyecharts 中的 Bar 类用于柱状图的绘制
from pyecharts import options as opts
import os
import webbrowser

def count(excel, col_name):
    return excel[col_name].value_counts()

def help_line(data):
    a_data = data.to_numpy()
    total = a_data.sum()
    rate = np.round((a_data / total * 1000), 2).tolist()
    return rate

def render_line(xdata, yname, ydata):
    line = (
        Line()
        .add_xaxis(xdata)
        .add_yaxis(yname, ydata, yaxis_index=1)
    )
    return line

def render_bar(xdata, yname ,ydata, title_opts=None):
    bar = (Bar(init_opts=opts.InitOpts(width="1000px", height="750px"))
           .add_xaxis(xdata)
           .add_yaxis(yname, ydata, yaxis_index=0, color="#9A7BFF")
           .extend_axis(
               yaxis=opts.AxisOpts(
                   type_="value",
                   name="占比",
                   position="right",
                   offset=10,
                   axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#00B0CF")
                    ),
                   axislabel_opts=opts.LabelOpts(formatter="{value}‰")
               )
           )
           .set_global_opts(yaxis_opts=opts.AxisOpts(
                                name="数量",
                                position="left",
                                offset=10,
                                axisline_opts=opts.AxisLineOpts(
                                        linestyle_opts=opts.LineStyleOpts(color="#9A7BFF")
                                    ),
                            ),
                            title_opts=title_opts,
                            datazoom_opts=opts.DataZoomOpts(),
                            legend_opts=
                                opts.LegendOpts(is_show=False),
                            tooltip_opts=
                                opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                            )
           )
    return bar


excel =  pd.read_excel("2024年普通高校招生专业选考科目要求.xlsx")   # 读取表格文件
# excel.info()

outlier_index = []  # 异常值的索引
for ind, province in excel["省份"].items(): # 在省份这一列中循环获取元素
    if province == "省份":  # 如果值为省份就将它的索引值记录
        outlier_index.append(ind)

excel.drop(outlier_index, inplace=True)   # 将这些值删除, 并覆盖原DataFrame
excel.reset_index(drop=True, inplace=True)  # 重新设置索引值，并覆盖原DtaFrame
excel.dropna(subset=["省份"],inplace=True)
province_amount = count(excel, "省份")   # 各省份高校数量
major_required = count(excel, "选考科目要求")
level = count(excel, "层次")


page = Page(page_title="高校数据分析",layout=Page.SimplePageLayout)

map1 = (
    Map(init_opts=opts.InitOpts(width="1000px", height="750px"))
    .add("高校数量", [list(z) \
    for z in zip(province_amount.index.tolist(),province_amount.to_list())], "china")
    .set_global_opts(title_opts=
                        opts.TitleOpts(title="2024年普通高校招生专业选考科目要求分析", pos_left="center"),
                     visualmap_opts=
                        opts.VisualMapOpts(max_=max(province_amount.to_list()), min_=min(province_amount.to_list())),
                     legend_opts=
                        opts.LegendOpts(is_show=False),
                    )
)

bar1 = render_bar(major_required.index.tolist(),
                  "数量", major_required.to_list())
bar2 = render_bar(level.index.tolist(),
                  "数量", level.to_list())
# 制作占比折线图
rate1 = help_line(major_required)
line1 = render_line(major_required.index.to_list(),
                    "占比", rate1)
rate2 = help_line(level)
line2 = render_line(level.index.tolist(),
                   "占比", rate2)

# 图表叠加
bar1.overlap(line1)
bar2.overlap(line2)

page.add(map1, bar1, bar2)
page.render("college.html")

webbrowser.open("file://" + os.path.realpath("college.html"))