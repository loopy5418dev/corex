import pkgutil
import importlib

def register_routes(app):
    for module in pkgutil.iter_modules(__path__):
        mod = importlib.import_module(f"{__name__}.{module.name}")
        if hasattr(mod, "bp"):
            app.register_blueprint(mod.bp)