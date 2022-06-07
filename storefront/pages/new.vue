<template>
  <div>
    <div class="level">
      <div class="level-left">
        <p class="level-item">
          <span class="is-size-5 has-text-weight-semibold">Add Products</span>
        </p>
        <p class="level-item">
          <span class="tag is-dark has-text-weight-semibold"
            >{{ products.length }} Item</span
          >
        </p>
      </div>
      <div class="level-right"></div>
    </div>

    <div class="box" v-for="(item, index) in products" :key="index">
      <div class="level">
        <div class="level-left">
          <p
            class="level-item is-size-4 has-text-grey-light has-text-weight-bold"
          >
            {{ index + 1 }}.
          </p>
          <div class="level-item is-size-4 has-text-grey-light"></div>
        </div>
        <div class="level-right">
          <button
            class="button is-danger"
            v-show="index != 0"
            @click="deleteItem(index)"
          >
            <b-icon icon="delete" class="mr-3" />Delete
          </button>
        </div>
      </div>
      <div class="columns is-variable is-8">
        <div class="column">
          <!-- Info Product -->
          <div class="field">
            <div class="control">
              <label for class="label">Preselect Data from Master</label>
              <b-autocomplete
                icon="chevron-down"
                v-model="item.query_master"
                placeholder="Select"
                :keep-first="true"
                :open-on-focus="true"
                :data="autocompleteMaster(index)"
                field="name"
                @select="(option) => getMaster(option, index)"
              ></b-autocomplete>
            </div>
          </div>
          <hr />
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
                <editor-menu-bar
                  :editor="editors[index].editor"
                  v-slot="{ commands, isActive }"
                >
                  <div class="menubar">
                    <div
                      class="toolbar"
                      style="
                        border: 1px solid #eee;
                        padding: 0.75rem 0.75rem;
                        border-radius: 5px;
                      "
                    >
                      <button
                        class="button is-info is-light"
                        @click="commands.undo"
                      >
                        <b-icon icon="undo-variant"></b-icon>
                      </button>

                      <button
                        class="button is-info is-light"
                        @click="commands.redo"
                      >
                        <b-icon icon="redo-variant"></b-icon>
                      </button>

                      <button
                        class="button is-info is-light"
                        :class="{ 'is-active': isActive.bold() }"
                        @click="commands.bold"
                      >
                        <b-icon icon="format-bold"></b-icon>
                      </button>

                      <button
                        class="button is-info is-light"
                        :class="{ 'is-active': isActive.italic() }"
                        @click="commands.italic"
                      >
                        <b-icon icon="format-italic"></b-icon>
                      </button>

                      <button
                        class="button is-info is-light"
                        :class="{ 'is-active': isActive.strike() }"
                        @click="commands.strike"
                      >
                        <b-icon icon="format-strikethrough"></b-icon>
                      </button>

                      <button
                        class="button is-info is-light"
                        :class="{ 'is-active': isActive.underline() }"
                        @click="commands.underline"
                      >
                        <b-icon icon="format-underline"></b-icon>
                      </button>
                      <button
                        class="button is-info is-light"
                        :class="{ 'is-active': isActive.heading({ level: 3 }) }"
                        @click="commands.heading({ level: 3 })"
                      >
                        <b-icon icon="format-title"></b-icon>
                      </button>
                      <button
                        class="button is-info is-light"
                        :class="{ 'is-active': isActive.paragraph() }"
                        @click="commands.paragraph"
                      >
                        <b-icon icon="format-align-justify"></b-icon>
                      </button>

                      <button
                        class="button is-info is-light"
                        @click="
                          commands.createTable({
                            rowsCount: 2,
                            colsCount: 2,
                            withHeaderRow: false,
                          })
                        "
                      >
                        <b-icon icon="table-plus"></b-icon>
                      </button>

                      <span v-if="isActive.table()">
                        <button
                          class="button is-light"
                          @click="commands.deleteTable"
                        >
                          <b-icon icon="table-remove"></b-icon>
                        </button>
                        <button
                          class="button is-light"
                          @click="commands.addRowAfter"
                        >
                          <b-icon icon="table-row-plus-after"></b-icon>
                        </button>

                        <button
                          class="button is-light"
                          @click="commands.deleteRow"
                        >
                          <b-icon icon="table-row-remove"></b-icon>
                        </button>
                      </span>
                    </div>
                  </div>
                </editor-menu-bar>
                <editor-content
                  class="editor__content"
                  :editor="editors[index].editor"
                />
              </div>
            </div>
            <br />
            <div class="field-body is-horizontal">
              <div class="field">
                <div class="control">
                  <label for class="label">Qty</label>
                  <input
                    type="text"
                    class="input"
                    v-model="item.qty"
                    placeholder="Qty"
                  />
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <label for class="label">Weight</label>
                  <input
                    type="text"
                    class="input"
                    v-model="item.weight"
                    placeholder="Weight"
                  />
                </div>
              </div>
            </div>
            <br />
            <div class="control">
              <label for class="label">SKU</label>
              <input
                type="text"
                class="input"
                v-model="item.sku"
                placeholder="Enter SKU"
              />
            </div>
            <br />
            <div class="field-body is-horizontal">
              <div class="field">
                <div class="control">
                  <label for class="label">Pricing</label>
                  <input
                    type="text"
                    class="input"
                    v-model="item.price"
                    placeholder="Price"
                  />
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
                  <input
                    type="text"
                    class="input"
                    v-model="item.type"
                    placeholder="Type"
                  />
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <label for class="label">Tags</label>
                  <input
                    type="text"
                    class="input"
                    v-model="item.tags"
                    placeholder="Tags"
                  />
                </div>
              </div>
            </div>
            <br />
            <div class="field">
              <div class="control">
                <label for class="label">HSN</label>
                <input
                  type="text"
                  class="input"
                  v-model="item.hsn"
                  placeholder="Tags"
                />
              </div>
            </div>
            <hr />
            <div class="field">
              <div
                v-for="(var_item, index_var) in item.variants"
                :key="index_var"
              >
                <div class="field-body is-horizontal">
                  <b-field :label="'Option #' + Number(index_var + 1)">
                    <b-input
                      placeholder="Option Name"
                      v-model="var_item.option"
                    ></b-input>
                  </b-field>
                  <b-field label="Price">
                    <b-input
                      placeholder="Option Price"
                      v-model="var_item.price"
                    ></b-input>
                  </b-field>
                  <b-field label="Qty">
                    <b-input
                      placeholder="Option Qty"
                      v-model="var_item.qty"
                    ></b-input>
                  </b-field>
                  <b-field label="Action">
                    <button
                      class="button is-danger is-light"
                      @click="removeOpt(index_var, index)"
                    >
                      <b-icon icon="close"></b-icon>
                    </button>
                  </b-field>
                </div>
                <br />
              </div>

              <div class="control">
                <button
                  class="button is-info is-light"
                  @click="addVariant(index)"
                >
                  <b-icon icon="plus" class="mr-3"></b-icon>Add Variants
                </button>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-5">
          <ImageUpload v-model="item.files" />
        </div>
      </div>
      <hr />

      <!-- <p
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
      Advanced Information
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
        </div>
      </div>-->
    </div>

    <br />
    <nav
      class=""
      style="padding: 0.5rem 0 0.5rem 0"
      :class="{ 'is-hidden': submitLoad }"
    >
      <div class="buttons">
        <button class="button" @click="createNew">
          <b-icon icon="plus-box-outline" class="mr-3" />Create New
        </button>
        <button class="button is-primary is-light" @click="createCopy">
          <b-icon icon="content-copy" class="mr-3" />Create Copy
        </button>
        <button class="level-item button is-info" @click="submit()">
          <b-icon icon="check-circle" class="mr-3" />Save
        </button>
      </div>
    </nav>
    <nav
      class="navbar is-mobile is-fixed-bottom has-shadow has-text-centered"
      style="padding: 0.5rem 0 0.5rem 0"
      :class="{ 'is-hidden': !submitLoad }"
    >
      <div class="container">
        <p class="navbar-item">
          <button class="button has-text-weight-medium is-success is-light">
            Uploading Products to Shopify . Grab a ☕ while we do the work.
          </button>
        </p>
        <p class></p>
      </div>
    </nav>

    <b-loading
      :is-full-page="true"
      :active.sync="submitLoad"
      :can-cancel="false"
    ></b-loading>
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
  History,
} from "tiptap-extensions";

export default {
  components: {
    ImageUpload,
    EditorContent,
    EditorMenuBar,
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
          variants: [],
          seo: {
            title: null,
            description: null,
          },
          google: {
            category: null,
            gender: null,
            labels: null,
            condition: null,
          },
          errors: {},
        },
      ],

      advanced: [{ show: false }],
    };
  },
  computed: {},
  mounted() {
    this.initEditor(0);
    let self = this;
    this.$axios
      .get("/get/master")
      .then(function (response) {
        console.log(response.data);
        self.products[0].data_master = response.data;
        self.base_master = response.data;
      })
      .catch(function (error) {
        self.$buefy.snackbar.open({
          duration: 4000,
          message: "Unable to fetch data for Master",
          type: "is-light",
          position: "is-top-right",
          actionText: "Close",
          queue: true,
          onAction: () => {
            self.isActive = false;
          },
        });
      });
  },
  methods: {
    removeOpt(index_var, index) {
      console.log(index_var, index);
      this.products[index].variants.splice(index_var, 1);
    },
    addVariant(index) {
      this.products[index].variants.push({
        option: "",
        price: 0,
        qty: this.products[index].qty,
      });
    },
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
            resizable: true,
          }),
          new TableHeader(),
          new TableCell(),
          new TableRow(),
        ],

        content: content,
      });
    },
    autocompleteMaster(index) {
      if (this.products[index].data_master.length != 0) {
        let data = this.products[index].data_master.filter((option) => {
          return (
            option.name
              .toString()
              .toLowerCase()
              .indexOf(this.products[index].query_master.toLowerCase()) >= 0
          );
        });
        console.log(data);
        return data;
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
        reader.onload = function (event) {
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
        let variants = JSON.parse(option.variants);
        variants.forEach((item) => {
          this.products[index].variants.push({
            option: item.option,
            price: item.price,
            qty: this.products[index].qty,
          });
        });
      }
    },
    deleteItem: function (index) {
      this.products[index].files.splice(index, 1);
      this.products[index].imageUrlArray.splice(index, 1);
    },
    clearUploads() {},
    createNew() {
      this.advanced.push({
        show: false,
      });
      this.editors.push({
        editor: null,
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
        hsn: null,
        variants: [],

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
        show: false,
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
        variants: baseItem.variants,

        seo: {
          title: baseItem.seo.title,
          description: baseItem.seo.description,
        },
        google: {
          category: baseItem.google.category,
          gender: baseItem.google.gender,
          labels: baseItem.google.labels,
          condition: baseItem.google.condition,
        },
      });
      this.editors.push({
        editor: null,
      });
      this.initEditor(this.products.length - 1);
      this.editors[this.products.length - 1].editor.setContent(
        this.editors[0].editor.getHTML()
      );
    },
    deleteItem(index) {
      this.products.splice(index, 1);
      this.advanced.splice(index, 1);
      this.editors.splice(index, 1);
    },
    submit() {
      let self = this;
      this.submitLoad = true;
      let formData = new FormData();
      this.products.forEach(function (element, i) {
        // self.editors[i].editor = element.editor;
        element.description = self.editors[i].editor.getHTML();
      });
      let payload = Object.assign([], this.products);

      payload.forEach((element) => {
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
            "Content-Type": "multipart/form-data",
          },
        })
        .then(function (response) {
          self.submitLoad = false;
          if (response.data.success) {
            self.$buefy.snackbar.open({
              duration: 4000,
              message: response.data.success,
              type: "is-light",
              position: "is-top-right",
              actionText: "Close",
              queue: true,
              onAction: () => {
                self.isActive = false;
              },
            });
          }
          if (response.data.message) {
            self.$buefy.snackbar.open({
              duration: 4000,
              message: response.data.message,
              type: "is-light",
              position: "is-top-right",
              actionText: "Close",
              queue: true,
              onAction: () => {
                self.isActive = false;
              },
            });
          }
        })
        .catch(function (error) {
          self.submitLoad = false;

          console.log(error);
        });
    },
  },
};
</script>

<style>
.noti-x {
  border: 1px solid lightblue;
  border-top: 5px solid lightblue;
  border-radius: 0 0 10px 10px;
  background-color: #fff;
}
</style>