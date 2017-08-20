# -*- coding: utf-8 -*-
import click
import json

from kawasemi.kawasemi import Kawasemi


@click.command()
@click.argument("message")
@click.option("config", '--config', type=click.Path(),
              default="kawasemirc.json",
              help="Path to the configuration file")
def main(message, config):
    with open(config) as f:
        config = json.load(f)
    kawasemi = Kawasemi(config)
    kawasemi.send(message)
