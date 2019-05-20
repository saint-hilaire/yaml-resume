from cerberus import Validator
from yaml_resume import schema
import yaml


def validate(resume):
    v = Validator(schema.resume)
    document = yaml.load(
        open(resume, 'r'),
        Loader=yaml.FullLoader
        )
    return (v.validate(document), v.errors)
