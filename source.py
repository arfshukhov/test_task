opening_html_tag = "<html>"

default_style_set = """
<style>

#header {
    background-color:blue;
    text-align:center;
    color: white   
}

#sidebar_left {
    background-color: lightblue;
    position: absolute;
    width: 15%;
    height: 100%;
    left: 0.5%;
    z-index: 1;
    top: 5%;    
}
#sidebar_right {
    background-color: lightblue;
    position: absolute;
    width: 15%;
    height: 100%;
    left: 84.5%;
    z-index: 1;
    top: 5%; 
}  

#footer {
    background-color:cyan;
    clear:both;
    text-align:center;
    padding:10px;    
}

</style>"""

header = """<head>
    <div id="header">
    <h1>Редактор форм</h1>
    </div>

</head>"""

open_workspace = """<body>
<div>
<div id="sidebar_left"></div>"""

close_workspace = """<div id="sidebar_right"></div>
</div>"""

footer = """<div id="footer"></div>
</body>"""

add_space_buttons = """
<div style="position: absolute; width: 120%; left: 18%; z-index: 2">
<form action="">
</div>
"""

closer_html_tag = "</html>"



