<template>
  <div>
    <div class="level">
      <div class="level-left">
        <p class="level-item">
          <span class="title">Add Products</span>
        </p>
        <p class="level-item">
          <span
            class="tag is-large is-info is-light has-text-weight-semibold"
          >{{ products.length }} Item</span>
        </p>
      </div>
      <div class="level-right"></div>
    </div>

    <div class="box" v-for="( item , index ) in products" :key="index">
      <div class="level">
        <div class="level-left">
          <p class="is-size-4 has-text-grey-light has-text-weight-bold">{{ index+1 }}.</p>
        </div>
        <div class="level-right">
          <button class="button is-danger is-light" v-show="index != 0" @click="deleteItem(index)">
            <span class="icon icon-btn">
              <feather type="x" size="1.3rem" />
            </span>
            Delete
          </button>
        </div>
      </div>
      <div class="columns">
        <div class="column">
          <!-- Info Product -->
          <div class="field">
            <div class="control">
              <label for class="label">Product Title</label>
              <input
                type="text"
                class="input"
                v-model="item.title"
                placeholder="Enter Product Title"
              />
            </div>
            <br />
            <div class="control">
              <label for class="label">Description</label>
              <textarea
                type="text"
                class="textarea"
                v-model="item.description"
                placeholder="Enter Description"
              />
            </div>
            <br />
            <div class="field-body is-horizontal">
              <div class="field">
                <div class="control">
                  <label for class="label">Qty</label>
                  <input type="text" class="input" v-model="item.qty" placeholder="Qty" />
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <label for class="label">Weight</label>
                  <input type="text" class="input" v-model="item.weight" placeholder="Weight" />
                </div>
              </div>
            </div>
            <br />
            <div class="control">
              <label for class="label">SKU</label>
              <input type="text" class="input" v-model="item.sku" placeholder="Enter SKU" />
            </div>
            <br />
            <div class="field-body is-horizontal">
              <div class="field">
                <div class="control">
                  <label for class="label">Pricing</label>
                  <input type="text" class="input" v-model="item.pricing" placeholder="Price" />
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <label for class="label">Cost Price</label>
                  <input
                    type="text"
                    class="input"
                    v-model="item.cost_price"
                    placeholder="Cost Price"
                  />
                </div>
              </div>
            </div>
            <br />
            <div class="field">
              <div class="control">
                <label for class="label">Product handle</label>
                <input type="text" class="input" v-model="item.handle" placeholder="Product Handle" />
              </div>
            </div>
            <br />
            <div class="field-body is-horizontal">
              <div class="field">
                <div class="control">
                  <label for class="label">Type</label>
                  <input type="text" class="input" v-model="item.type" placeholder="Type" />
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <label for class="label">Tags</label>
                  <input type="text" class="input" v-model="item.tags" placeholder="Tags" />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-5">
          <label for class="label">Upload Images</label>
          <ImageUpload  v-model="item.files" />
        </div>
      </div>
      <hr />

      <p
        class="has-text-centered is-marginless has-text-link has-text-weight-semibold is-fullwidth"
        @click="advanced[index].show = !advanced[index].show"
        style="cursor:pointer;"
      >
        Show Advance Information
        <span class="icon icon-btn">
          <feather v-if="advanced[index].show == true" type="chevron-down" />
          <feather v-if="advanced[index].show == false" type="chevron-up" />
        </span>
      </p>
      <!-- Advanced Information -->
      <div v-show="advanced[index].show">
        <div class="columns">
          <div class="column">
            <p class="is-size-4 has-text-weight-bold">SEO</p>
            <br />
            <div class="field">
              <div class="control">
                <label for class="label">SEO Title</label>
                <input type="text" v-model="item.seo.title" class="input" />
              </div>
            </div>
            <div class="field">
              <div class="control">
                <label for class="label">SEO Description</label>
                <textarea name class="textarea" v-model="item.seo.description" />
              </div>
            </div>
          </div>
        </div>
        <div class="columns">
          <div class="column">
            <p class="is-size-4 has-text-weight-bold">Google Shopping Information</p>
            <br />
            <div class="field">
              <div class="control">
                <label for class="label">Category</label>
                <input type="text" class="input" v-model="item.google.category" />
              </div>
            </div>
            <div class="field">
              <div class="control">
                <label for class="label">Gender</label>
                <input name class="input" v-model="item.google.gender" />
              </div>
            </div>
            <div class="field">
              <div class="control">
                <label for class="label">Labels</label>
                <input name class="input" v-model="item.google.labels" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <br />
    <nav class="navbar is-mobile is-fixed-bottom has-shadow" style="padding: 0.5rem 0 0.5rem 0;">
      <div class="container">
        <div class="navbar-brand">
          <p class="navbar-item">
            <button class="button is-primary is-light" @click="createNew">
              <span class="icon icon-btn">
                <feather type="plus" size="1.3rem" />
              </span>
              Create New
            </button>
          </p>
          <p class="navbar-item">
            <button class="button is-black is-light" @click="createCopy">
              <span class="icon icon-btn">
                <feather type="copy" size="1.3rem" />
              </span>
              Create Copy
            </button>
          </p>
          <p class="navbar-item">
            <button class="level-item button is-link is-light">
              <span class="icon icon-btn">
                <feather type="check" size="1.3rem" />
              </span>
              Save
            </button>
          </p>
        </div>
      </div>
    </nav>
  </div>
</template>


<script>
import axios from 'axios';
import ImageUpload from '@/components/ImageUpload';

export default {
  components:{
       ImageUpload
      },
  data(){
    return {
      files: [],
      products : [
        {
          files: null,
          imageUrlArray: [] ,
          title: null,
          description: null,
          qty: null,
          weight: null,
          sku: null,
          pricing: null,
          cost_price: null,
          handle: null,
          image_alt_text: null,
          type: null,
          tags: null,
          seo: {
          title: null,
          description: null,
          },
          google: {
          category: null,
          gender: null,
          labels: null,
          condition: null,
          }
        }
      ],
      
      advanced: [
        { show : false }
      ]
    }
  },
  mounted(){
    let self = this    
  },
  methods:{
     listUploads(e , index) {
       console.log(index)
            this.showUploads = true;
            let files = e.srcElement.files;


            let self = this;

            for (var index = 0; index < files.length; index++) {
                // generate a new FileReader object
                var reader = new FileReader();
                self.products[index].files.push(files[index])
                // inject an image with the src url
                reader.onload = function (event) {
                    const imageUrl = event.target.result;
                    // const thumb = document.querySelectorAll('.thumb')[index];
                    self.products[index].imageUrlArray.push(imageUrl);
                }

                // when the file is read it triggers the onload 
                // event above.
                reader.readAsDataURL(files[index]);
            }
        },
        deleteItem: function (index) {

            this.products[index].files.splice(index, 1)
            this.products[index].imageUrlArray.splice(index, 1)


        },
        clearUploads() {
           
        },
      createNew(){
      this.advanced.push({
        show:false
      })
      this.products.push( {
          files: null,
          imageUrlArray: [] ,
          title: null,
          description: null,
          qty: null,
          weight: null,
          sku: null,
          pricing: null,
          cost_price: null,
          handle: null,
          image_alt_text: null,
          type: null,
          tags: null,
          seo: {
          title: null,
          description: null,
          },
          google: {
          category: null,
          gender: null,
          labels: null,
          condition: null,
          }
      })
    },
    createCopy(){
      let baseItem = this.products[0]
      console.log(baseItem)
      this.advanced.push({
        show:false
      })
      this.products.push( {
          title: baseItem.title,
          description: baseItem.description,
          qty: baseItem.qty,
          weight: baseItem.weight,
          sku: baseItem.sku,
          pricing: baseItem.pricing,
          cost_price: baseItem.cost_price,
          handle: baseItem.handle,
          image_alt_text: baseItem.image_alt_text,
          type: baseItem.type,
          tags: baseItem.tags,
          seo: {
          title: baseItem.seo.title,
          description: baseItem.seo.description,
          },
          google: {
          category: baseItem.google.category,
          gender: baseItem.google.gender,
          labels: baseItem.google.labels,
          condition: baseItem.google.condition,
          }
      })
    },
    deleteItem(index){
      this.products.splice( index , 1)
      this.advanced.splice( index , 1)
    }
  }

  
}
</script>