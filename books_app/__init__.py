from flask import Flask, render_template, redirect, request
app = Flask(__name__)
app.secret_key = "seecrett"