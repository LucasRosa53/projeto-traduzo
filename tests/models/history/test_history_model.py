import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    response_json = json.loads(HistoryModel.list_as_json())
    assert "text_to_translate" in response_json[1]
    assert "translate_from" in response_json[1]
    assert "translate_to" in response_json[1]
    assert "Do you love music?" in response_json[1].values()
    assert "en" in response_json[1].values()
    assert "pt" in response_json[1].values()
