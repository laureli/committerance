import os
import json

from flask import Flask, render_template, send_from_directory, request, redirect, jsonify, g, \
session, flash, url_for, abort

from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

from model import Cookie, User, dbsession
from forms import LoginForm, SignupForm