use sqlx::{ postgres::PgPoolOptions, mysql::MySqlPoolOptions };

#[tokio::main]
async fn main() -> Result<(), sqlx::Error> {
    let pool = PgPoolOptions::new()
        .connect("postgres://hsdb:hsdbpass@localhost:5432/hstestdb")
        .await?;

    let result: Vec<(String, String)> = sqlx::query_as("SELECT * FROM HTML")
        .fetch_all(&pool)
        .await?;

    for row in result {
        println!("{} {}", row.0, row.1);
    }

    Ok(())
}
