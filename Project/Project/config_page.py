import flask, flask_login

def config_page(name: str, url: str):
    def render_template(function: object):
        def processor(*args, **kwargs):
            context = function(*args, **kwargs)
            if context["message"] == "Successfully":
                return flask.redirect(url)
            return flask.render_template(
                template_name_or_list= name,
                current_user= flask_login.current_user,
                **context
            )
        return processor
    return render_template
