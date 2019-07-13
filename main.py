import os
from bottle import (get, post, redirect, request, route, run, static_file, template, error)
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
    display_shows = [json.loads(utils.getJsonFromFile(someshows)) for someshows in utils.AVAILABE_SHOWS]

    m = display_shows[0]
    y = m["summary"]
    print(y)
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=display_shows)


@route('/ajax/show/<showid>/episode/<episodeid>')
def show_episode(showid, episodeid):
    sectionTemplate = "./templates/episode.tpl"
    sectionData = utils.get_episode(showid, episodeid)
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=sectionData)

@route('/ajax/show/', method="get")
def find_show():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/search', method="get")
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/search', method="post")
def test():
    name_search = request.forms.get("q")
    string_search = (str.split(name_search))
    display_shows = [json.loads(utils.getJsonFromFile(someshows)) for someshows in utils.AVAILABE_SHOWS]
    m = display_shows[0]
    y = m["name"]
    k = m["summary"]
    x = [m]
    t = x[0]['_embedded']['episodes'][0]
    print(t)

    string_search2 = (str.split(y))
    string_search3 = (str.split(k))
    for r in string_search:

        for k in string_search2:
            if r == k:
                print(r)
                print(k)
                return "hey"


@route('/episode', method="get")
def browse():
    sectionTemplate = "./templates/episode.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/ajax/show/<filename>')
def show(filename):
    sectionTemplate = "./templates/show.tpl"

    showfirst = utils.getShow(filename)
    testnewEpisode = showfirst['_embedded']
    print(showfirst['_embedded']['episodes'][0])
    print(showfirst)

    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=showfirst)


@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/show', method="get")
def browse():
    sectionTemplate = "./templates/show.tpl"

    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=sectionData)


def main():
    run(host="localhost", port=os.environ.get('PORT', 7009))



if __name__ == '__main__':
    main()
