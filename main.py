import os
from bottle import (get, post, redirect, request, route, run, static_file, template,error)
import utils
import json




# Static Routes

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")


@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")


@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/browse', method="get")
def browse():
    x = [utils.getJsonFromFile("7")]
    y = json.loads(x[0])

    print (x)

    display_shows = [json.loads(utils.getJsonFromFile(someshows)) for someshows in utils.AVAILABE_SHOWS]
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=display_shows)



@route('/search', method="get")
def browse():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})

@route('/search', method="post")
def test():
    sectionTemplate = "./templates/search.tpl"
    name_search = request.forms.get("q")
    return name_search

@route('/episode', method="get")
def browse():
    sectionTemplate = "./templates/episode.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})

@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})

@route('/show', method="get")
def browse():
    sectionTemplate = "./templates/show.tpl"

    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


def main():
    run(host="localhost", port=os.environ.get('PORT', 7009))


# def main ():
#     run(host='0.0.0.0', port=os.environ.get('PORT', 5000))

if __name__ == '__main__':
    main()
