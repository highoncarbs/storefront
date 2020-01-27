<template>
  <div>
    <div class="notification">
      <div class="field is-grouped is-grouped-multiline">
        <div class="control">
          <div class="file">
            <label class="file-label">
              <input
                class="file-input"
                @change.prevent="listUploads"
                accept="image/*"
                type="file"
                name="ref-file"
                multiple
              />
              <span class="file-cta">
                <span class="file-icon">
                  <feather type="upload" size="1rem"></feather>
                </span>
                <span class="file-label">Choose a file…</span>
              </span>
            </label>
          </div>
        </div>
        <div class="control">
          <button class="button is-danger is-light" @click="clearUploads">
            <span class="file-icon">
              <feather type="x" size="1rem"></feather>
            </span>
            Clear
          </button>
        </div>
      </div>
      <br />
      <ul>
        <article class="media" v-for="(file , index) in files" :key="index">
          <figure class="media-left">
            <p class="image is-128x128" style="height: auto !important;">
              <img class="image-preview" v-bind:src="imageUrlArray | getIndexedImage(index)" />
            </p>
          </figure>
          <div class="media-content">
            <div class="content">
              <p class="has-text-weight-bold">
                <span class="has-text-grey">{{ index +1 }}.</span>
                {{ file.name }}
                <br />
                <span class="has-text-grey has-text-weight-normal">
                  File size: {{file.size |
                  formatBytes }}
                </span>
              </p>
            </div>
          </div>
          <div class="media-right">
            <button class="delete" @click.prevent="deleteItem(index)"></button>
          </div>
        </article>
      </ul>
    </div>
  </div>
</template>

<script>
    export default {
           props: {
        },
        data() {
            return {
                imageData: null ,
                files : [],
                imageUrlArray : []

            }
        },
        watch: {
          files: function(){
            this.$emit( 'input' , this.files)
          }
        },
        filters: {
            getIndexedImage(val, index) {
                // console.log(`This: ${val}`);
                return val[index];
            },

            formatBytes(a, b) {
                if (0 == a) return "0 Bytes";
                var c = 1024,
                    d = b || 2,
                    e = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"],
                    f = Math.floor(Math.log(a) / Math.log(c));
                return parseFloat((a / Math.pow(c, f)).toFixed(d)) + " " + e[f]
            }
        },
        methods: {

            listUploads(e) {
                let files = e.srcElement.files;


                let self = this;

                for (var index = 0; index < files.length; index++) {
                // generate a new FileReader object
                    var reader = new FileReader();
                    self.files.push(files[index])
                    // inject an image with the src url
                    reader.onload = function (event) {
                        const imageUrl = event.target.result;
                        // const thumb = document.querySelectorAll('.thumb')[index];
                        self.imageUrlArray.push(imageUrl);
                    }

                    // when the file is read it triggers the onload 
                    // event above.
                    reader.readAsDataURL(files[index]);
            }
             
        }, 
         deleteItem: function (index) {

            this.files.splice(index, 1)
            this.imageUrlArray.splice(index, 1)


        },
        clearUploads() {
            this.imageUrlArray = []
            this.files = []

        },
        
    }  
}
</script>

<style>
.image-input {
  display: block;
  width: 200px;
  height: 200px;
  cursor: pointer;
  background-size: cover;
  background-position: center center;
}

.placeholder {
  border-radius: 3px;
  background: #f0f0f0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.button-icon {
  border-radius: 50%;
  padding: 10px 10px 5px 10px;
  background-color: rgba(0, 0, 0, 0.5);
}
.placeholder-x {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.placeholder:hover {
  background: #e0e0e0;
}

.file-input {
  display: none;
}
</style>