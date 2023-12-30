from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Union

app = FastAPI()

crypto_prices: Dict[str, Dict[str, Union[int, float]]] = {
    "BTC": {"price": 50000, "volume_24h": 60000000},
    "ETH": {"price": 3000, "volume_24h": 40000000},
}

class CryptoRequest(BaseModel):
    amount: float

class CryptoResponse(BaseModel):
    crypto_id: str
    amount: float
    value: float

def validate_crypto_id(crypto_id: str) -> None:
    """Validates the format of crypto_id."""
    if not isinstance(crypto_id, str):
        raise HTTPException(status_code=400, detail="crypto_id deve ser uma string")
    if crypto_id not in crypto_prices:
        raise HTTPException(status_code=404, detail="Criptomoeda não encontrada")

def get_crypto_price_data(crypto_id: str) -> Dict[str, Union[int, float]]:
    """Gets data of a specific cryptocurrency."""
    validate_crypto_id(crypto_id)
    return crypto_prices[crypto_id]

def validate_crypto_request(crypto_id: str, amount: float) -> None:
    """Validates the crypto request."""
    validate_crypto_id(crypto_id)
    if amount <= 0:
        raise HTTPException(status_code=400, detail="A quantidade deve ser maior que zero")

@app.get("/")
def read_root() -> Dict[str, str]:
    """Rota raiz para exibir uma mensagem de boas-vindas."""
    return {"message": "Bem-vindo ao analisador financeiro de criptomoedas!"}

@app.get("/crypto/{crypto_id}")
def get_crypto_data(crypto_id: str) -> Dict[str, Union[int, float]]:
    """Gets data of a specific cryptocurrency."""
    return get_crypto_price_data(crypto_id)

@app.get("/crypto/{crypto_id}/calculate_value")
def calculate_value(crypto_id: str, amount: float) -> Dict[str, Union[str, float]]:
    """Calculates the value of a specific amount of cryptocurrency."""
    validate_crypto_request(crypto_id, amount)
    price_data = get_crypto_price_data(crypto_id)
    price = price_data["price"]
    value = price * amount
    return {"crypto_id": crypto_id, "amount": amount, "value": value}

@app.post("/crypto/{crypto_id}/calculate_value_with_model")
def calculate_value_with_model(crypto_id: str, crypto_request: CryptoRequest) -> CryptoResponse:
    """Calculates the value of a specific amount of cryptocurrency using a Pydantic model."""
    amount = crypto_request.amount
    validate_crypto_request(crypto_id, amount)
    price_data = get_crypto_price_data(crypto_id)
    price = price_data["price"]
    value = price * amount
    return CryptoResponse(crypto_id=crypto_id, amount=amount, value=value)

if __name__ == "__main__":
    import uvicorn
    import logging

    logging.basicConfig(level=logging.INFO)

    uvicorn.run(app, host="127.0.0.1", port=8000)
