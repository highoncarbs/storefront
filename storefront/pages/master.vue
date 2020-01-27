<template>
  <div>
    <div class="level">
      <div class="level-left">
        <p class="level-item">
          <span class="title">New Master</span>
        </p>
      </div>
      <div class="level-right"></div>
    </div>

    <div class="columns">
      <div class="column is-8">
        <div class="box">
          <div class="field">
            <div class="control">
              <label for class="label">Product Title</label>
              <input
                type="text"
                class="input"
                v-model="form.title"
                placeholder="Enter Product Title"
              />
            </div>
            <br />
            <div class="control">
              <label for class="label">Description</label>
              <div class="editor">
                <editor-menu-bar :editor="editor" v-slot="{ commands, isActive }">
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
                    <span class="tag is-info">in KG</span>
                  </label>
                  <input type="text" class="input" v-model="form.weight" placeholder="Weight" />
                </div>
              </div>
            </div>
            <br />
            <div class="control">
              <label for class="label">
                SKU
                <span class="tag is-info">Prefix of SKU</span>
              </label>
              <input type="text" class="input" v-model="form.sku" placeholder="Enter SKU" />
            </div>
            <br />
            <div class="field-body is-horizontal">
              <div class="field">
                <div class="control">
                  <label for class="label">Pricing</label>
                  <input type="text" class="input" v-model="form.pricing" placeholder="Price" />
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <label for class="label">Cost Price</label>
                  <input
                    type="text"
                    class="input"
                    v-model="form.cost_price"
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
                  <input type="text" class="input" v-model="form.type" placeholder="Type" />
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <label for class="label">
                    Tags
                    <span class="tag is-info">Separate by commas</span>
                  </label>
                  <input type="text" class="input" v-model="form.tags" placeholder="Tags" />
                </div>
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
            <button class="level-item button is-link is-light" @click="submit">
              <span class="icon icon-btn">
                <feather type="check" size="1.3rem" />
              </span>
              Save
            </button>
          </p>
          <p class="navbar-item">
            <button class="button is-primary is-light" @click="createNew">
              <span class="icon icon-btn">
                <feather type="x" size="1.3rem" />
              </span>
              Clear
            </button>
          </p>
        </div>
      </div>
    </nav>
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
      editor: null,
      files: [],
      advanced: [{ show: false }],

      form: {
        title: null,
        description: null,
        qty: null,
        weight: null,
        sku: null,
        pricing: null,
        cost_price: null,
        type: null,
        tags: null
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
        pricing: null,
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
        pricing: baseItem.pricing,
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
      let formData = this.form 
      formData.description = this.editor.getHTML();
      this.axios.post('/add/master' , JSON.stringify(formData))
        .then( function(response){
          
        })
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