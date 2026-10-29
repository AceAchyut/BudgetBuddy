
# backend/app/security.py

import os
from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

SECRET_KEY = os.environ.get("BUDGETBUDDY_SECRET_KEY")

if not SECRET_KEY:
    # Local development only. Set BUDGETBUDDY_SECRET_KEY
    # to a strong random secret before deploying.
    SECRET_KEY = "dev-only-change-this-secret-before-deployment"

ALGORITHM = "HS256"
ACCESS_TOKEN_MINUTES = 15
REFRESH_TOKEN_DAYS = 7

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_token(user_id: int, token_type: str, expires_delta: timedelta) -> str:
    now = datetime.now(timezone.utc)

    payload = {
        "sub": str(user_id),
        "type": token_type,
        "iat": now,
        "exp": now + expires_delta,
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def create_access_token(user_id: int) -> str:
    return create_token(
        user_id,
        "access",
        timedelta(minutes=ACCESS_TOKEN_MINUTES),
    )


def create_refresh_token(user_id: int) -> str:
    return create_token(
        user_id,
        "refresh",
        timedelta(days=REFRESH_TOKEN_DAYS),
    )


def decode_token(token: str, expected_type: str) -> dict:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    if payload.get("type") != expected_type:
        raise jwt.InvalidTokenError("Incorrect token type")

    if not payload.get("sub"):
        raise jwt.InvalidTokenError("Missing subject")

    return payload
