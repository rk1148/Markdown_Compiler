const tokens = marked.lexer(markdown, options);
console.log(marked.parser(tokens, options));
const lexer = new marked.Lexer(options);
const tokens = lexer.lex(markdown);
console.log(tokens);
console.log(lexer.tokenizer.rules.block); // block level rules used
console.log(lexer.tokenizer.rules.inline); // inline level rules used
console.log(marked.Lexer.rules.block); // all block level rules
console.log(marked.Lexer.rules.inline); // all inline level rules
$ node
> require('marked').lexer('> I am using marked.')
[
  {
    type: "blockquote",
    raw: "> I am using marked.",
    tokens: [
      {
        type: "paragraph",
        raw: "I am using marked.",
        text: "I am using marked.",
        tokens: [
          {
            type: "text",
            raw: "I am using marked.",
            text: "I am using marked."
          }
        ]
      }
    ]
  },
  links: {}
]
import { marked } from 'marked';

const md = `
  # heading

  [link][1]

  [1]: #heading "heading"
`;

const tokens = marked.lexer(md);
console.log(tokens);

const html = marked.parser(tokens);
console.log(html);
// Create reference instance
import { marked } from 'marked';

// Override function
const renderer = {
  heading(text, level) {
    const escapedText = text.toLowerCase().replace(/[^\w]+/g, '-');

    return `
            <h${level}>
              <a name="${escapedText}" class="anchor" href="#${escapedText}">
                <span class="header-link"></span>
              </a>
              ${text}
            </h${level}>`;
  }
};

marked.use({ renderer });

// Run marked
console.log(marked.parse('# heading+'));
// Create reference instance
import { marked } from 'marked';

// Override function
const tokenizer = {
  codespan(src) {
    const match = src.match(/^\$+([^\$\n]+?)\$+/);
    if (match) {
      return {
        type: 'codespan',
        raw: match[0],
        text: match[1].trim()
      };
    }

    // return false to use original codespan tokenizer
    return false;
  }
};

marked.use({ tokenizer });

// Run marked
console.log(marked.parse('$ latex code $\n\n` other code `'));
import { marked } from 'marked';

// Override function
const walkTokens = (token) => {
  if (token.type === 'heading') {
    token.depth += 1;
  }
};

marked.use({ walkTokens });

// Run marked
console.log(marked.parse('# heading 2\n\n## heading 3'));
import { marked } from 'marked';
import fm from 'front-matter';

// Override function
const hooks = {
  preprocess(markdown) {
    const { attributes, body } = fm(markdown);
    for (const prop in attributes) {
      if (prop in this.options) {
        this.options[prop] = attributes[prop];
      }
    }
    return body;
  }
};

marked.use({ hooks });

// Run marked
console.log(marked.parse(`
---
headerIds: false
---

## test
`.trim()));
// Create reference instance
import { marked } from 'marked';

// Override function
const tokenizer = {
  codespan(src) {
    const match = src.match(/^\$+([^\$\n]+?)\$+/);
    if (match) {
      return {
        type: 'codespan',
        raw: match[0],
        text: match[1].trim()
      };
    }

    // return false to use original codespan tokenizer
    return false;
  }
};

marked.use({ tokenizer });

// Run marked
console.log(marked.parse('$ latex code $\n\n` other code `'));
import { marked } from 'marked';

// Override function
const walkTokens = (token) => {
  if (token.type === 'heading') {
    token.depth += 1;
  }
};

marked.use({ walkTokens });

// Run marked
console.log(marked.parse('# heading 2\n\n## heading 3'));
import { marked } from 'marked';
import fm from 'front-matter';

// Override function
const hooks = {
  preprocess(markdown) {
    const { attributes, body } = fm(markdown);
    for (const prop in attributes) {
      if (prop in this.options) {
        this.options[prop] = attributes[prop];
      }
    }
    return body;
  }
};

marked.use({ hooks });

// Run marked
console.log(marked.parse(`
---
headerIds: false
---

## test
`.trim()));
const lexer = new marked.Lexer(options);
const tokens = lexer.lex(markdown);
console.log(tokens);
console.log(lexer.tokenizer.rules.block); // block level rules used
console.log(lexer.tokenizer.rules.inline); // inline level rules used
console.log(marked.Lexer.rules.block); // all block level rules
console.log(marked.Lexer.rules.inline); // all inline level rules
$ node
> require('marked').lexer('> I am using marked.')
[
  {
    type: "blockquote",
    raw: "> I am using marked.",
    tokens: [
      {
        type: "paragraph",
        raw: "I am using marked.",
        text: "I am using marked.",
        tokens: [
          {
            type: "text",
            raw: "I am using marked.",
            text: "I am using marked."
          }
        ]
      }
    ]
  },
  links: {}
]
import { marked } from 'marked';

const md = `
  # heading

  [link][1]

  [1]: #heading "heading"
`;

const tokens = marked.lexer(md);
console.log(tokens);

const html = marked.parser(tokens);
console.log(html);
