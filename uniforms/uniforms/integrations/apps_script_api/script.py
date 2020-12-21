from dataclasses import dataclass
from collections import namedtuple
from typing import Union, List


Parameter = namedtuple('Parameter', ['name', 'value'])

@dataclass
class AppsScript:
    name: str
    id: str

    def request(self, params: List[Parameter]) -> dict:
        request = {}
        request['function'] = self.name
        request['devMode'] = True
        request['parameters'] = []
        
        for parameter in params:
            request['parameters'].append({parameter.name: parameter.value})

        return request

scripts = [
    AppsScript(
        name='CheckEditorPermission',
        id='1ZUYlLBqUwAAgB6wIN715IuG5l4q8GzPgCFMc3aqQBWYykpnuZHMBLZFj'
    ),
    AppsScript(
        name='AssignTrigger2Form',
        id='1Es4B6fDpiq9EfmPUtnWtxRWZE45-CquQzucmGFkL4GI8hkcWB0dB8DXw'
    )
]