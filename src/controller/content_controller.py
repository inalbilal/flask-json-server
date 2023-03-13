import json
from flask import request, render_template, redirect, flash
from src.form.content_form import ContentForm
from src.service.json_server_service import JsonServerService
from src.trait.object_normalizer import Normalize


class ContentController:
    @staticmethod
    def create_json_content():
        form = ContentForm(request.form)
        if request.method == 'POST' and form.validate():
            try:
                json_server_service = JsonServerService()
                content = json_server_service.create_json_server(form)
                full_url = f"{request.url_root}{content.slug}/{content.endpoint}"
                flash(full_url)
            except Exception as e:
                flash(f"Failed {str(e)}")
            return redirect("/create-server")

        return render_template('content_form/index.html', form=form)

    @staticmethod
    def load_json_content(slug, endpoint):
        json_server_service = JsonServerService()
        json_server = json_server_service.load_json_server(slug, endpoint)
        return json.loads(json.dumps(json_server.content, cls=Normalize))
