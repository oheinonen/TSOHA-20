from flask import Flask
from flask import redirect, render_template
from flask import redirect, render_template, request, session


app = Flask(__name__)

import routes