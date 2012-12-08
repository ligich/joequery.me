# Personal website

from joequery.settings import FLASK_ENV, app
from flask import (
 request, g, abort, flash, redirect, 
 render_template, url_for
)
import joequery.static_pages.routes
import joequery.blog.routes
app.register_blueprint(joequery.blog.routes.bp)
app.register_blueprint(joequery.static_pages.routes.bp)

@app.before_request
def before_first_request():
  # Grant access to the dev/production environment variable
  def get_env():
    g.env = FLASK_ENV

  # Determine cloudfront vs local assets delivery
  def set_assets_dir():
    if FLASK_ENV == "production":
      g.assets = "https://s3.amazonaws.com/assets.joequery.me"
    else:
      g.assets = app.static_url_path

  get_env()
  set_assets_dir()
  

@app.errorhandler(404)
def page_not_found(e):
      return render_template('404.html'), 404
