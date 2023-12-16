use sqlx::{ postgres::{PgPoolOptions, PgRow}, Connection, PgConnection, Row, Postgres, PgPool };
use futures::TryStreamExt;

#[derive(sqlx::FromRow)]
struct Html {
    uuid: String,
    content: String,
}

async fn list_html(connection: &mut PgConnection) -> Result<Vec<Html>, sqlx::Error> {
    let mut rows = sqlx::query("SELECT * FROM HTML").fetch(connection);
    let mut pages: Vec<Html> = Vec::new();

    while let Some(row) = rows.try_next().await? {
        let uuid: String = row.try_get("uuid")?;
        let content: String = row.try_get("content")?;
        
        pages.push(Html { uuid, content });

    }

    Ok(pages)
}

async fn list_html_v2(connection: &mut PgConnection) -> Result<Vec<Html>, sqlx::Error> {
    sqlx::query("SELECT * FROM HTML")
        .try_map(|row: PgRow| Ok(
            Html { 
                uuid: row.try_get("uuid")?,
                content: row.try_get("content")?,
            }
        ))
        .fetch_all(connection)
        .await
}

async fn list_html_v3(connection: &mut PgConnection) -> Result<Vec<Html>, sqlx::Error> {
    sqlx::query_as::<Postgres, Html>("SELECT * FROM HTML")
        .fetch_all(connection)
        .await
}

async fn get_page(pool: &PgPool, uuid: &str) -> Result<Html, sqlx::Error> {
    sqlx::query_as::<Postgres, Html>("SELECT * FROM HTML WHERE uuid=$1")
        .bind(uuid)
        .fetch_one(pool)
        .await
}

#[tokio::main]
async fn main() -> Result<(), sqlx::Error> {
    let url = "postgres://hsdb:hsdbpass@localhost:5432/hstestdb";
    let mut connection = PgConnection::connect(&url).await?;

    for page in list_html(&mut connection).await? {
        println!("{}: {}", page.uuid, page.content);
    }

    for page in list_html_v2(&mut connection).await? {
        println!("{}: {}", page.uuid, page.content);
    }

    for page in list_html_v3(&mut connection).await? {
        println!("{}: {}", page.uuid, page.content);
    }

    let pool = PgPoolOptions::new()
        .connect("postgres://hsdb:hsdbpass@localhost:5432/hstestdb")
        .await?;

    let uuid = "550e8400-e29b-41d4-a716-446655440000";
    let page = get_page(&pool, uuid).await?;

    println!("{}: {}", page.uuid, page.content);

    Ok(())
}


