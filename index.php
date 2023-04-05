<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
</head>

<body>
    <form action="index.php" method="get" float="center" class="container-sm bg-primary text-white pt-5 pb-5">
      <div class="mt-3 mb-3">
        <label for="words" class="form-label">Enter the English words to translate here:</label>
        <input type="textarea" class="form-control" name="words" placeholder="Enter English Words To Translate To Here">
        <input type="submit" class="btn btn-primary">
      </div>
    </form>

  <?php 
    $words = $_GET["words"];
    echo $words
  ?>
</body>

</html>