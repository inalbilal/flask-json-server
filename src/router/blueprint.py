from flask import Blueprint as BP
from src.controller.content_controller import ContentController


class Blueprint:
    @staticmethod
    def routes():
        blueprint = BP('blueprint', __name__)
        blueprint.route('/create-server', methods=['GET', 'POST'])(ContentController.create_json_content)
        blueprint.route('/<path:slug>/<path:endpoint>', methods=['GET', 'POST'])(ContentController.load_json_content)
        return blueprint
