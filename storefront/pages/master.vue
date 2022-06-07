<template>
  <div>
    <div class="level">
      <div class="level-left">
        <p class="level-item">
          <span class="title">Master</span>
        </p>
      </div>
      <div class="level-right">
        <p class="level-item">
          <button @click="loadData" class="button is-light">
            <b-icon icon="eye" class="icon-btn"></b-icon>
            <span>View</span>
          </button>
        </p>
      </div>
    </div>
    <div v-if="view" class="box" style="padding:2.5rem">
      <div class="field">
        <div class="control">
          <label for class="label">Product Title</label>
          <input type="text" class="input" v-model="form.title" placeholder="Enter Product Title" />
        </div>
        <br />
        <div class="control">
          <label for class="label">Description</label>
          <div class="editor">
            <editor-menu-bar :editor="editor" v-slot="{ commands, isActive }">
              <div class="menubar">
                <div
                  class="toolbar"
                  style="border:1px solid #eee; padding: 0.75rem 0.75rem; border-radius: 5px"
                >
                  <button class="button is-info is-light" @click="commands.undo">
                    <b-icon icon="undo-variant"></b-icon>
                  </button>

                  <button class="button is-info is-light" @click="commands.redo">
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
                    @click="commands.createTable({rowsCount: 2, colsCount: 2, withHeaderRow: false })"
                  >
                    <b-icon icon="table-plus"></b-icon>
                  </button>

                  <span v-if="isActive.table()">
                    <button class="button is-light" @click="commands.deleteTable">
                      <b-icon icon="table-remove"></b-icon>
                    </button>
                    <button class="button is-light" @click="commands.addRowAfter">
                      <b-icon icon="table-row-plus-after"></b-icon>
                    </button>

                    <button class="button is-light" @click="commands.deleteRow">
                      <b-icon icon="table-row-remove"></b-icon>
                    </button>
                  </span>
                </div>
              </div>
            </editor-menu-bar>
            <editor-content class="editor__content" :editor="editor" />
          </div>
        </div>
        <br />
        <div class="field-body is-horizontal">
          <div class="field">
            <div class="control">
              <label for class="label">Qty</label>
              <input type="text" class="input" v-model="form.qty" placeholder="Qty" />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <label for class="label">
                Weight
                <span class="tag is-info is-light">in KG</span>
              </label>
              <input type="text" class="input" v-model="form.weight" placeholder="Weight" />
            </div>
          </div>
        </div>
        <br />
        <div class="control">
          <label for class="label">
            SKU
            <span class="tag is-info is-light">Prefix of SKU</span>
          </label>
          <input type="text" class="input" v-model="form.sku" placeholder="Enter SKU" />
        </div>
        <br />
        <div class="field-body is-horizontal">
          <div class="field">
            <div class="control">
              <label for class="label">price</label>
              <input type="text" class="input" v-model="form.price" placeholder="Price" />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <label for class="label">Cost Price</label>
              <input type="text" class="input" v-model="form.cost_price" placeholder="Cost Price" />
            </div>
          </div>
        </div>
        <br />

        <div class="field-body is-horizontal">
          <div class="field">
            <div class="control">
              <label for class="label">Type</label>
              <input type="text" class="input" v-model="form.type" placeholder="Type" />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <label for class="label">
                Tags
                <span class="tag is-info is-light">Separate by commas</span>
              </label>
              <input type="text" class="input" v-model="form.tags" placeholder="Tags" />
            </div>
          </div>
        </div>
        <br />
        <div class="field">
          <div class="control">
            <label for class="label">
              HSN Code
              <span class="tag is-info is-light">Required for Customs</span>
            </label>
            <input type="text" class="input" v-model="form.hsn" placeholder="HSN Code : eg. 62140" />
          </div>
        </div>
        <hr />
        <div class="field">
          <div v-for="(var_item, index) in form.variants" :key="index">
            <div class="field-body is-horizontal">
              <b-field label="Option">
                <b-input v-model="var_item.option"></b-input>
              </b-field>
              <b-field label="Price">
                <b-input v-model="var_item.price"></b-input>
              </b-field>
            </div>
            <br />
          </div>

          <div class="control">
            <button class="button is-info is-light" @click="addVariant(index)">
              <b-icon icon="plus" class="icon-btn"></b-icon>Add Variants
            </button>
          </div>
        </div>
      </div>
      <hr />
      <div class="buttons">
        <button class="level-item button is-info" @click="submit">
          <b-icon icon="check-circle" class="icon-btn" />Save
        </button>
        <button class="button is-info is-light" @click="createNew">
          <b-icon icon="delete" class="icon-btn" />Clear
        </button>
      </div>
    </div>

    <div v-if="!view" class="box">
      <b-table :data="data">
        <template >
          <b-table-column v-slot="props" field="name" label="Name">{{props.row.name}}</b-table-column>
          <b-table-column v-slot="props" field="product_type" label="Type">{{props.row.product_type}}</b-table-column>
          <b-table-column v-slot="props"field="tags" label="Tags">{{props.row.tags}}</b-table-column>
          <b-table-column v-slot="props"field="price" label="Price">{{props.row.price}}</b-table-column>
          <b-table-column v-slot="props"field label="Action">
            <div class="buttons">
              <div class="button is-info is-light is-small">
                <b-icon icon="eye"></b-icon>
              </div>
              <div class="button is-small is-danger is-light">
                <b-icon icon="delete"></b-icon>
              </div>
            </div>
          </b-table-column>
        </template>
      </b-table>
    </div>

    <br />

    <br />
  </div>
</template>


<script>
import axios from "axios";

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
    EditorContent,
    EditorMenuBar
  },
  data() {
    return {
      data: [],
      view: true,
      loading: false,
      editor: null,
      files: [],
      advanced: [{ show: false }],

      form: {
        title: null,
        description: null,
        qty: null,
        weight: null,
        sku: null,
        price: null,
        cost_price: null,
        type: null,
        tags: null,
        hsn: null,
        variants: []
      }
    };
  },
  mounted() {
    let self = this;
    this.editor = new Editor({
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
      content: `
          <p>Hand Block Printed Bagru Stole</p>
    <table width="100%">
    <tbody>
    <tr>
    <td>Fabric</td>
    <td> 100% Linen Cotton</td>
    </tr>
    <tr>
    <td>Dimensions</td>
    <td>38 x 71 inch</td>
    </tr>
    <tr>
    <td>Color</td>
    <td>Blue</td>
    </tr>
    </tbody>
    </table>
    <p>This product is handcrafted by skilled artisans for you and may have slight irregularities that are a natural outcome of the human involvement in the process.<br></p>
    <p>Because each piece is made by hand , no two are exactly alike.</p>
    <p>The colors seen in the image may vary from the actual product due to different computer screen resolutions and displays.</p>
    <h3>Craft - Bagru Hand Block Printing</h3>
    <p>About the craft.</p>
        `
    });
  },

  methods: {
    addVariant(index) {
      this.form.variants.push({ option: "", price: 0 });
    },
    loadData() {
      this.view = !this.view;
      this.loading = true;
      let self = this;
      this.$axios.get("/get/master").then(response => {
        console.log(response.data)
        self.data = response.data;
        self.loading = false;
      });
    },
    beforeDestroy() {
      this.editor.destroy();
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
          // const thumb = document.querySelectorAll('.thumb')[index];
          self.products[index].imageUrlArray.push(imageUrl);
        };

        // when the file is read it triggers the onload
        // event above.
        reader.readAsDataURL(files[index]);
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
      this.products.push({
        files: null,
        imageUrlArray: [],
        title: null,
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
        seo: {
          title: null,
          description: null
        },
        google: {
          category: null,
          gender: null,
          labels: null,
          condition: null
        }
      });
    },
    createCopy() {
      let baseItem = this.products[0];
      console.log(baseItem);
      this.advanced.push({
        show: false
      });
      this.products.push({
        title: baseItem.title,
        description: baseItem.description,
        qty: baseItem.qty,
        weight: baseItem.weight,
        sku: baseItem.sku,
        price: baseItem.price,
        cost_price: baseItem.cost_price,
        handle: baseItem.handle,
        image_alt_text: baseItem.image_alt_text,
        type: baseItem.type,
        tags: baseItem.tags,
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
    },
    deleteItem(index) {
      this.products.splice(index, 1);
      this.advanced.splice(index, 1);
    },
    submit() {
      let self = this;
      let formData = this.form;
      formData.description = this.editor.getHTML();
      this.$axios
        .post("/add/master", JSON.stringify(formData), {
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(function(response) {
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
              }
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
              }
            });
          }
        });
    }
  }
};
</script>
<style>
.ProseMirror {
  margin-top: 1rem;
  padding: 2rem 1.5rem;
  border: 0.5px solid lightgray;
  border-radius: 5px;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.07);
}

.editor {
  position: relative;
  max-width: 100%;
  /* margin: 0 auto 5rem auto; */
}
.editor__content {
  overflow-wrap: break-word;
  word-wrap: break-word;
  word-break: break-word;
}
.editor__content * {
  caret-color: currentColor;
}
.editor__content pre {
  padding: 0.7rem 1rem;
  border-radius: 5px;
  background: #000;
  color: #fff;
  font-size: 0.8rem;
  overflow-x: auto;
}
.editor__content pre code {
  display: block;
}
.editor__content p code {
  display: inline-block;
  padding: 0 0.4rem;
  border-radius: 5px;
  font-size: 0.8rem;
  font-weight: bold;
  background: rgba(0, 0, 0, 0.1);
  color: rgba(0, 0, 0, 0.8);
}
.editor__content ul,
.editor__content ol {
  padding-left: 1rem;
}
.editor__content h3 {
  font-weight: 700;
  font-size: 1.5rem;
}
.editor__content li > p,
.editor__content li > ol,
.editor__content li > ul {
  margin: 0;
}
.editor__content a {
  color: inherit;
}
.editor__content blockquote {
  border-left: 3px solid rgba(0, 0, 0, 0.1);
  color: rgba(0, 0, 0, 0.8);
  padding-left: 0.8rem;
  font-style: italic;
}
.editor__content blockquote p {
  margin: 0;
}
.editor__content img {
  max-width: 100%;
  border-radius: 3px;
}
.editor__content table {
  border-collapse: collapse;
  table-layout: fixed;
  width: 100%;
  margin: 0;
  overflow: hidden;
}
.editor__content table td,
.editor__content table th {
  min-width: 1em;
  border: 0.5px solid lightgrey;
  padding: 3px 5px;
  vertical-align: top;
  box-sizing: border-box;
  position: relative;
}
.editor__content table td > *,
.editor__content table th > * {
  margin-bottom: 0;
}
.editor__content table th {
  font-weight: bold;
  text-align: left;
}
.editor__content table .selectedCell:after {
  z-index: 2;
  position: absolute;
  content: "";
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background: rgba(200, 200, 255, 0.4);
  pointer-events: none;
}
.editor__content table .column-resize-handle {
  position: absolute;
  right: -2px;
  top: 0;
  bottom: 0;
  width: 4px;
  z-index: 20;
  background-color: #adf;
  pointer-events: none;
}
.editor__content .tableWrapper {
  margin: 1em 0;
  overflow-x: auto;
}
.editor__content .resize-cursor {
  cursor: ew-resize;
  cursor: col-resize;
}
</style>