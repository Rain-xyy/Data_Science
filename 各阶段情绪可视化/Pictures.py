import pyecharts.options as opts
from pyecharts.charts import Radar

v1 = [[0.38857893, 0.16573679, 0.156547424, 0.124056449, 0.070561208, 0.052838858, 0.041680341]]

(
    Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC"))
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="希望", max_=0.5),
            opts.RadarIndicatorItem(name="高兴", max_=0.5),
            opts.RadarIndicatorItem(name="崇敬", max_=0.5),
            opts.RadarIndicatorItem(name="伤心", max_=0.5),
            opts.RadarIndicatorItem(name="怀疑", max_=0.5),
            opts.RadarIndicatorItem(name="恐慌", max_=0.5),
            opts.RadarIndicatorItem(name="愤怒", max_=0.5),
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="#fff"),
    )
    .add(
        series_name="Third-Stage:2020.2.10-2020.2.13",
        data=v1,
        linestyle_opts=opts.LineStyleOpts(color="#CD0000"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="情绪雷达图"), legend_opts=opts.LegendOpts()
    )
    .render("情绪雷达图Third-Stage.html")
)
