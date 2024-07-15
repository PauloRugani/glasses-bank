class DataModel:
    msg: str = ''
    data: str = ''

    @classmethod
    def model_data(cls, model_result) -> dict:
        import json
        
        try:
            load_json = json.loads(model_result.json())
        
            cls.msg = load_json[0]['ctx']['error']
            cls.data = load_json[0]['input']

        except Exception:
            cls.msg = ''
            cls.data = model_result

        dict_erros = {
            'msg' : cls.msg,
            'text' : cls.data
        }

        return dict_erros