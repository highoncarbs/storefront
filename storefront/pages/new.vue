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
          <p class="level-item is-size-4 has-text-grey-light has-text-weight-bold">{{ index+1 }}.</p>
          <div class="level-item is-size-4 has-text-grey-light"></div>
        </div>
        <div class="level-right">
          <button class="button is-danger is-light" v-show="index != 0" @click="deleteItem(index)">
            <b-icon icon="delete" class="icon-btn" />Delete
          </button>
        </div>
      </div>
      <div class="columns">
        <div class="column">
          <!-- Info Product -->
          <div class="field notification has-background-info-light">
            <div class="control">
              <label for class="label">Preselect Data from Master</label>
              <b-autocomplete
                v-model="item.query_master"
                placeholder="Select"
                :keep-first="true"
                :open-on-focus="true"
                :data="autocompleteMaster(index)"
                field="name"
                @select="option => getMaster(option,index)"
              ></b-autocomplete>
            </div>
          </div>
          <div class="field">
            <div class="control">
              <label for class="label">Product Title</label>
              <input
                type="text"
                class="input"
                v-model="item.name"
                placeholder="Enter Product Title"
              />
            </div>
            <br />
            <div class="control">
              <label for class="label">Description</label>
              <div class="editor">
                <editor-menu-bar :editor="editors[index].editor" v-slot="{ commands, isActive }">
                  <div class="menubar">
                    <div class="toolbar">
                      <button class="button is-small" @click="commands.undo">
                        <feather size="1rem" type="corner-up-left" />
                      </button>

                      <button class="button is-small" @click="commands.redo">
                        <feather size="1rem" type="corner-up-right" />
                      </button>

                      <button
                        class="button is-small"
                        :class="{ 'is-active': isActive.bold() }"
                        @click="commands.bold"
                      >
                        <feather size="1rem" type="bold" />
                      </button>

                      <button
                        class="button is-small"
                        :class="{ 'is-active': isActive.italic() }"
                        @click="commands.italic"
                      >
                        <feather size="1rem" type="italic" />
                      </button>

                      <button
                        class="button is-small"
                        :class="{ 'is-active': isActive.strike() }"
                        @click="commands.strike"
                      >
                        <feather size="1rem" type="minus" />
                      </button>

                      <button
                        class="button is-small"
                        :class="{ 'is-active': isActive.underline() }"
                        @click="commands.underline"
                      >
                        <feather size="1rem" type="underline" />
                      </button>
                      <button
                        class="button is-small"
                        :class="{ 'is-active': isActive.heading({ level: 3 }) }"
                        @click="commands.heading({ level: 3 })"
                      >
                        <feather size="1rem" type="type" />
                      </button>
                      <button
                        class="button is-small"
                        :class="{ 'is-active': isActive.paragraph() }"
                        @click="commands.paragraph"
                      >
                        <feather size="1rem" type="align-justify" />
                      </button>

                      <button
                        class="button is-small"
                        @click="commands.createTable({rowsCount: 2, colsCount: 2, withHeaderRow: false })"
                      >
                        <feather size="1rem" type="grid" />
                      </button>

                      <span v-if="isActive.table()">
                        <button class="button is-small" @click="commands.deleteTable">
                          <feather size="1rem" type="x-square" />
                        </button>
                        <button class="button is-small" @click="commands.addRowAfter">
                          <feather size="1rem" type="plus-circle" />
                        </button>

                        <button class="button is-small" @click="commands.deleteRow">
                          <feather size="1rem" type="x-circle" />
                        </button>
                      </span>
                    </div>
                  </div>
                </editor-menu-bar>
                <editor-content class="editor__content" :editor="editors[index].editor" />
              </div>
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
                  <input type="text" class="input" v-model="item.price" placeholder="Price" />
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
            <br />
            <div class="field">
              <div class="control">
                <label for class="label">HSN</label>
                <input type="text" class="input" v-model="item.hsn" placeholder="Tags" />
              </div>
            </div>
          </div>
        </div>
        <div class="column is-5">
          <ImageUpload v-model="item.files" />
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
        <!-- <div class="columns">
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
        </div>-->
      </div>
    </div>

    <br />
    <nav
      class="navbar is-mobile is-fixed-bottom has-shadow"
      style="padding: 0.5rem 0 0.5rem 0;"
      :class="{'is-hidden': submitLoad}"
    >
      <div class="container">
        <div class="navbar-brand">
          <p class="navbar-item">
            <button class="button is-primary is-light" @click="createNew">
              <b-icon icon="plus-box-outline" class="icon-btn" />Create New
            </button>
          </p>
          <p class="navbar-item">
            <button class="button is-black is-light" @click="createCopy">
              <b-icon icon="content-copy" class="icon-btn" />Create Copy
            </button>
          </p>
          <p class="navbar-item">
            <button class="level-item button is-link is-light" @click="submit()">
              <b-icon icon="checkbox-marked-outline" class="icon-btn" />Save
            </button>
          </p>
        </div>
      </div>
    </nav>
    <nav
      class="navbar is-mobile is-fixed-bottom has-shadow has-text-centered"
      style="padding: 0.5rem 0 0.5rem 0;"

      :class="{'is-hidden': !submitLoad}"
    >
      <div class="container ">
         <p class="navbar-item">
            <button class="button has-text-weight-medium is-success is-light" >
              Uploading Products to Shopify . Grab a ☕ while we do the work.

            </button>
          </p>
          <p  class="">
          </p>
      </div>
    </nav>

    <b-loading :is-full-page="true" :active.sync="submitLoad" :can-cancel="false">
      
    </b-loading>
  </div>
</template>


<script>
import axios from "axios";
import ImageUpload from "@/components/ImageUpload";

import { Editor, EditorContent, EditorMenuBar } from "tiptap";
import {
  Blockquote,
  CodeBlock,
  HardBreak,
  Heading,
  OrderedList,
  BulletList,
  ListItem,
  TodoItem,
  TodoList,
  Bold,
  Code,
  Italic,
  Link,
  Table,
  TableHeader,
  TableCell,
  TableRow,
  Strike,
  Underline,
  History
} from "tiptap-extensions";

export default {
  components: {
    ImageUpload,
    EditorContent,
    EditorMenuBar
  },
  data() {
    return {
      submitLoad: false,
      files: [],
      base_master: [],
      editors: [{ editor: null }],
      products: [
        {
          // editor: null,
          data_master: [],
          query_master: "",
          files: null,
          imageUrlArray: [],
          name: null,
          description: null,
          qty: null,
          weight: null,
          sku: null,
          price: null,
          cost_price: null,
          handle: null,
          image_alt_text: null,
          type: null,
          tags: null,
          hsn: null,
          seo: {
            title: null,
            description: null
          },
          google: {
            category: null,
            gender: null,
            labels: null,
            condition: null
          },
          errors: {}
        }
      ],

      advanced: [{ show: false }]
    };
  },
  computed: {},
  mounted() {
    this.initEditor(0);
    let self = this;
    this.$axios
      .get("/get/master")
      .then(function(response) {
        console.log(response.data);
        self.products[0].data_master = response.data;
        self.base_master = response.data;
      })
      .catch(function(error) {
        self.$buefy.snackbar.open({
          duration: 4000,
          message: "Unable to fetch data for Master",
          type: "is-light",
          position: "is-top-right",
          actionText: "Close",
          queue: true,
          onAction: () => {
            self.isActive = false;
          }
        });
      });
  },
  methods: {
    initEditor(index, content) {
      let self = this;
      this.editors[index].editor = new Editor({
        extensions: [
          new Blockquote(),
          new BulletList(),
          new CodeBlock(),
          new HardBreak(),
          new Heading({ levels: [1, 2, 3] }),
          new ListItem(),
          new OrderedList(),
          new TodoItem(),
          new TodoList(),
          new Link(),
          new Bold(),
          new Code(),
          new Italic(),
          new Strike(),
          new Underline(),
          new History(),
          new Table({
            resizable: true
          }),
          new TableHeader(),
          new TableCell(),
          new TableRow()
        ],

        content: content
      });
    },
    autocompleteMaster(index) {
      if (this.products[index].data_master.length != 0) {
        return this.products[index].data_master.filter(option => {
          return (
            option.name
              .toString()
              .toLowerCase()
              .indexOf(this.products[index].query_master.toLowerCase()) >= 0
          );
        });
      }
    },
    listUploads(e, index) {
      console.log(index);
      this.showUploads = true;
      let files = e.srcElement.files;

      let self = this;

      for (var index = 0; index < files.length; index++) {
        // generate a new FileReader object
        var reader = new FileReader();
        self.products[index].files.push(files[index]);
        // inject an image with the src url
        reader.onload = function(event) {
          const imageUrl = event.target.result;
          console.log(imageUrl);
          // const thumb = document.querySelectorAll('.thumb')[index];
          self.products[index].imageUrlArray.push(imageUrl);
        };

        // when the file is read it triggers the onload
        // event above.
        reader.readAsDataURL(files[index]);
      }
    },
    getMaster(option, index) {
      if (option != null) {
        this.products[index].name = option.name;
        this.products[index].qty = option.qty;
        this.products[index].weight = option.weight;
        this.products[index].sku = option.sku;
        this.products[index].price = option.price;
        this.products[index].cost_price = option.cost_price;
        this.products[index].type = option.product_type;
        this.products[index].tags = option.tags;
        this.products[index].hsn = option.hsn;
        this.editors[index].editor.setContent(option.description);
      }
    },
    deleteItem: function(index) {
      this.products[index].files.splice(index, 1);
      this.products[index].imageUrlArray.splice(index, 1);
    },
    clearUploads() {},
    createNew() {
      this.advanced.push({
        show: false
      });
      this.editors.push({
        editor: null
      });

      this.products.push({
        // editor: null,
        HSN: null,
        query_master: "",
        data_master: this.base_master,
        files: null,
        imageUrlArray: [],
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
        hsn: null
        // seo: {
        //   title: null,
        //   description: null
        // },
        // google: {
        //   category: null,
        //   gender: null,
        //   labels: null,
        //   condition: null
        // }
      });
      this.initEditor(this.products.length - 1, "");
    },
    createCopy() {
      let baseItem = this.products[0];
      console.log(baseItem);
      this.advanced.push({
        show: false
      });

      let new_product = this.products.push({
        editor: null,
        name: baseItem.name,
        qty: baseItem.qty,
        weight: baseItem.weight,
        sku: baseItem.sku,
        price: baseItem.price,
        cost_price: baseItem.cost_price,
        handle: baseItem.handle,
        image_alt_text: baseItem.image_alt_text,
        type: baseItem.type,
        tags: baseItem.tags,
        query_master: "",
        hsn: baseItem.hsn,
        data_master: this.base_master,
        seo: {
          title: baseItem.seo.title,
          description: baseItem.seo.description
        },
        google: {
          category: baseItem.google.category,
          gender: baseItem.google.gender,
          labels: baseItem.google.labels,
          condition: baseItem.google.condition
        }
      });
      this.editors.push({
        editor: null
      });
      this.initEditor(this.products.length - 1);
      this.editors[this.products.length - 1].editor.setContent(
        baseItem.editor.getHTML()
      );
    },
    deleteItem(index) {
      this.products.splice(index, 1);
      this.advanced.splice(index, 1);
    },
    submit() {
      let self = this;
      this.submitLoad = true;
      let formData = new FormData();
      this.products.forEach(function(element, i) {
        // self.editors[i].editor = element.editor;
        element.description = self.editors[i].editor.getHTML();
      });
      let payload = Object.assign([], this.products);

      payload.forEach(element => {
        element.imageUrlArray = null;
        element.errors = null;

        formData.append(
          "data_" + String(payload.indexOf(element)),
          JSON.stringify(element)
        );
        if (element.files != null) {
          for (var i = 0; i < element.files.length; i++) {
            let file = element.files[i];
            formData.append(
              "files_" + String(payload.indexOf(element) + "_") + i,
              element.files[i]
            );
          }
        }
      });
      console.log(JSON.stringify(formData));
      this.$axios
        .post("/add/product", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(function(response) {
          self.submitLoad = false;
          self.$buefy.snackbar.open({
            duration: 4000,
            message: response.data.message,
            type: "is-light",
            position: "is-top-right",
            actionText: "Close",
            queue: true,
            onAction: () => {
              self.isActive = false;
            }
          });
        })
        .catch(function(error) {
          self.submitLoad = false;

          console.log(error);
        });
    }
  }
};
</script>