<?php
class Html
{
    public $uuid;
    public $content;

    public function __construct($uuid, $content)
    {
        $this->uuid = $uuid;
        $this->content = $content;
    }

    public function __getUUID()
    {
        return $this->uuid;
    }

    public function __getContent()
    {
        return $this->content;
    }
}

function __list_html($connection)
{

    $stmt = $connection->query("SELECT * FROM HTML");
    //$stmt = $connection->prepare("SELECT * FROM HTML");
    //$stmt->execute();

    $pages = [];
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        $pages[] = new Html($row['uuid'], $row['content']);
    }

    return $pages;
}

/*  PDO::FETCH_ASSOC

    PDO::FETCH_ASSOC: devuelve un array indexado por los nombres de las columnas del conjunto de resultados

    Especifica que el método de obtención debe devolver cada fila como un array indexado 
    por los nombres de las columnas devueltos en el correspondiente conjunto de resultados. 
    Si éste contiene varias columnas con el mismo nombre, PDO::FETCH_ASSOC devuelve un único 
    valor por nombre de columna.
*/

function __get_page($connection, $uuid)
{

    $stmt = $connection->prepare("SELECT * FROM HTML WHERE uuid= :uuid");
    $stmt->bindValue(':uuid', $uuid);
    $stmt->execute();

    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    return $row['content'];

}

$url = "pgsql:host=localhost;port=5432;dbname=hstestdb;user=hsdb;password=hsdbpass";
$connection = new PDO($url);

$pages = __list_html($connection);
foreach ($pages as $page) {
    echo $page->__getUUID() . ": " . $page->__getContent() . "\n";
}

$uuid = "550e8400-e29b-41d4-a716-446655440000";
$pageContent = __get_page($connection, $uuid);
echo $uuid . ": " . $pageContent . "\n";

$connection = null;
?>