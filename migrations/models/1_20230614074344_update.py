from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;
        ALTER TABLE "message" ALTER COLUMN "payload" TYPE JSONB USING "payload"::JSONB;
        ALTER TABLE "message" ALTER COLUMN "payload" TYPE JSONB USING "payload"::JSONB;
        ALTER TABLE "message" ALTER COLUMN "payload" TYPE JSONB USING "payload"::JSONB;
        ALTER TABLE "message" ALTER COLUMN "payload" TYPE JSONB USING "payload"::JSONB;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TEXT USING "created_at"::TEXT;
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TEXT USING "created_at"::TEXT;
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TEXT USING "created_at"::TEXT;
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TEXT USING "created_at"::TEXT;
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TEXT USING "created_at"::TEXT;
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TEXT USING "created_at"::TEXT;
        ALTER TABLE "message" ALTER COLUMN "created_at" TYPE TEXT USING "created_at"::TEXT;
        ALTER TABLE "message" ALTER COLUMN "payload" TYPE TEXT USING "payload"::TEXT;
        ALTER TABLE "message" ALTER COLUMN "payload" TYPE TEXT USING "payload"::TEXT;
        ALTER TABLE "message" ALTER COLUMN "payload" TYPE TEXT USING "payload"::TEXT;
        ALTER TABLE "message" ALTER COLUMN "payload" TYPE TEXT USING "payload"::TEXT;"""
