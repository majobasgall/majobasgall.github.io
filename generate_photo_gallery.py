import os


def generate_gallery(images_folder):
    # Generate the HTML code for the photo gallery webpage
    html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Photo Gallery</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
  <style>
    /* Styling for the thumbnails */
    .thumbnail-container {
      position: relative;
      width: 100%;
      height: 0;
      padding-bottom: 100%; /* Set a fixed aspect ratio for the thumbnails (1:1 in this example) */
    }

    .thumbnail {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover; /* Crop the images to fit the thumbnail size while preserving aspect ratio */
      border: 2px solid #ccc;
      padding: 5px;
    }

    /* Styling for the modal carousel */
    .modal .carousel-item {
      max-height: 90vh;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h1 class="text-center">Photo Gallery</h1>
      </div>
    </div>

    <div class="row">
      <!-- Thumbnail grid -->
      <div class="col-md-12">
        <div class="row justify-content-center">'''

    # Iterate over the images in the folder
    index = 0
    for filename in os.listdir(images_folder):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".png"):
            image_path = os.path.join(images_folder, filename)
            thumbnail_code = f'''
          <div class="col-sm-6 col-md-4 col-lg-3">
            <div class="thumbnail-container">
              <img class="thumbnail img-fluid" src="{image_path}" alt="" data-index="{index}">
            </div>
          </div>'''
            html_code += thumbnail_code
            index += 1

    html_code += '''
        </div>
      </div>
    </div>
  </div>

  <!-- Modal slideshow -->
  <div class="modal fade" id="modal" tabindex="-1" role="dialog" aria-labelledby="modalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-body">
          <div id="carousel" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
              <!-- Add carousel indicators dynamically using JavaScript -->
            </ol>
            <div class="carousel-inner">
              <!-- Add carousel items dynamically using JavaScript -->
            </div>
            <a class="carousel-control-prev" href="#carousel" role="button" data-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carousel" role="button" data-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
  <script>
    $(document).ready(function() {
      // Load images into the modal carousel
      function loadCarouselImages(imagePaths) {
        var carouselIndicators = $(".carousel-indicators");
        var carouselItems = $(".carousel-inner");
        carouselIndicators.empty();
        carouselItems.empty();

        for (var i = 0; i < imagePaths.length; i++) {
          var imagePath = imagePaths[i];
          var activeClass = i === 0 ? "active" : "";

          var indicatorCode = `<li data-target="#carousel" data-slide-to="${i}" class="${activeClass}"></li>`;
          var carouselItemCode = `
            <div class="carousel-item ${activeClass}">
              <img class="d-block w-100" src="${imagePath}" alt="Slide ${i + 1}">
            </div>`;

          carouselIndicators.append(indicatorCode);
          carouselItems.append(carouselItemCode);
        }
      }

      // Open modal and load images into the carousel on thumbnail click
      $(".thumbnail-container").click(function() {
        var imagePaths = [];

        // Get all thumbnail images
        var thumbnails = $(".thumbnail");
        thumbnails.each(function() {
          imagePaths.push($(this).attr("src"));
        });

        loadCarouselImages(imagePaths);

        // Open the modal
        $("#modal").modal("show");

        // Enable carousel functionality
        $("#carousel").carousel();
      });
    });
  </script>
</body>
</html>'''

    return html_code


# Set the path to the "photos" folder
images_folder = "photos"

# Generate the HTML code for the photo gallery webpage
html_code = generate_gallery(images_folder)

# Write the HTML code to a file
with open("gallery_tmp.html", "w") as file:
    file.write(html_code)

print("Photo gallery webpage generated successfully!")
