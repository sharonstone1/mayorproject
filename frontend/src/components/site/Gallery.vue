<template>
    <div
      class="container"
      id="Gallery_details"
    >
      <h4 id="gallery">
        Gallery
      </h4>
      <p>
        Please be free to have a look on our gallery page. Most of the course here are our creation cooking
        ,they have not made by nobody in the restaurant world.
      </p><br>

      <div class="row">
        <div
          class="carousel slide col-8 offset-2"
          data-ride="carousel"
          id="carouselInterval"
        >
          <div class="carousel-inner">
            <div
              class="carousel-item active"
              data-interval="10000"
            >
              <img
                alt="burger no update"
                class="d-block w-100"
                src="static/media//imageplate5.jpg"
              >
            </div>

            <div class="carousel-item">
              <img
                alt="steak poulet no update"
                class="d-block w-100"
                src="static/media//haricot-vert-aux-steak-de-poulet.jpg"
              >
            </div>

            <div class="carousel-item">
              <img
                alt="image crevette no update"
                class="d-block w-100"
                src="static/media//legumes-vert-aux-crevettes.jpg"
              >
            </div>
            <div class="carousel-item">
              <img
                alt="image poulet no update"
                class="d-block w-100"
                src="static/media//poulet-braise-aux-crepes.jpg"
              >
            </div>
            <div class="carousel-item">
              <img
                alt="image frite no update"
                class="d-block w-100"
                src="static/media//frites-de-plaintain-aux-legumes-vert.jpg"
              >
            </div>
          </div>

          <a
            class="carousel-control-prev"
            data-slide="prev"
            href="#carouselInterval"
            role="button"
          >
            <span
              aria-hidden="true"
              class="carousel-control-prev-icon"
            />
            <span class="sr-only">Previous</span>
          </a>
          <a
            class="carousel-control-next"
            data-slide="next"
            href="#carouselInterval"
            role="button"
          >
            <span
              aria-hidden="true"
              class="carousel-control-next-icon"
            />
            <span class="sr-only">Next</span>
          </a>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Gallery'
}
</script>

<style scoped>

</style>
