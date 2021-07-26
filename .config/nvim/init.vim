"""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""
""""""    VIM configuraction         """"""""
""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""
set nocompatible
set encoding=utf-8
scriptencoding utf-8
filetype off
syntax enable

set showcmd
set mouse=a

set number 
set relativenumber

set tabstop=2
set softtabstop=2
set shiftwidth=2

set autoindent
set smarttab
set expandtab

" textwidth allows to auto wrap lines at 80th chars exactly
" Select the line and press gq to manually adjust to 80 chars
set textwidth=80

set wildmenu
set ruler

" Show matching braces pairs
set showmatch
set matchpairs+=¡:!

" Flash windows if an error ocurrs
set visualbell

" Diplay vertical line at char 80th
set colorcolumn=80,100
set cursorline 
"set cursorcolumn

" Shows '$' for end of line usefull to detect white spaces
"set list                             

" Seach configurations
set hlsearch
set smartcase
set ignorecase
set incsearch

" Split configuration
set splitbelow
set splitright

" Tab for autocomplete
inoremap <tab> <c-n>
inoremap <S-Tab> <c-N>

"""""""""""""""""""""""""""""""""""""""""""""
"    Mapping native commands to keys         "
"""""""""""""""""""""""""""""""""""""""""""""
let mapleader = ","

" Remapping keys for using WINDOWs in split mode
noremap <c-l> <c-w>l 
noremap <c-h> <c-w>h 
noremap <c-j> <c-w>j 
noremap <c-k> <c-w>k 

noremap <leader>L <c-w>L 
noremap <leader>H <c-w>H 
noremap <leader>J <c-w>J 
noremap <leader>k <c-w>K 

" Swap vertical windows
noremap <c-x> <c-w>x 
" Change vertical layout to horizontal
"noremap <c-a> <c-w>t<c-w>K 
" Change horizontal layout to vertical
"noremap <c-z> <c-w>t<c-w>H 

noremap <Right> :vertical resize +5 <cr>
noremap <Left> :vertical resize -5 <cr>
noremap <Up> :resize +5 <cr>
noremap <Down> :resize -5 <cr>

inoremap jj <Esc>
" Places the cursor after the )
inoremap aa <esc>2la
vnoremap <leader>eb :w! b.sql<cr>:vsp b.sql<cr>

noremap <leader>w :w<cr>                    " Save file faster
noremap <leader>q :q<cr>                    " exit file faster
noremap <leader>R :so $MYVIMRC<cr>          " Reload vimrc config
"noremap <leader>. :                         
noremap <leader>l :noh<cr>                  " Hide highlight from search
noremap <leader>n :set nu rnu<cr>           " Show numbers and relative numbers
noremap <leader>m :set nu nornu<cr>         " Show just numbers 
noremap <leader>N :set nonu nornu<cr>       " Hide numbers

" Search selected text
vnoremap <leader>s y /<c-r>"<cr>
" Search text in cursor place
noremap <leader>s ye /<c-r>"<cr>
" Replace text in cursor place
noremap <leader>F ye :%s/<c-r>"

" Disjoint lines and place cursos at the end of newline
noremap <leader>o i<return><esc>$

" Erase tildes from a, e,i,o,u and erase ñ 
noremap <leader>ti :%s/á/a/g<cr><bar>:%s/é/e/g<cr><bar>:%s/í/i/g<cr><bar>:%s/ó/o/g<cr><bar>:%s/ú/u/g<cr><bar>:%s/ñ/n/g<cr>
noremap <leader>co :read $HOME/.config/nvim/snippets/code-fence-asciidoc<cr>jo

function! Tab_Or_Complete()
  if col('.')>1 && strpart( getline('.'), col('.')-2, 3 ) =~ '^\w'
    return "\<C-N>"
  else
    return "\<Tab>"
  endif
endfunction
:inoremap <Tab> <C-R>=Tab_Or_Complete()<CR>

""""""""""""""""""""""""""""""""""""""""""""
"               Styling VIm                 "
"""""""""""""""""""""""""""""""""""""""""""""
" Vim Style configuration may have little dependencies
" Style the cursorline 
augroup cursorline
    au!
    au ColorScheme * hi clear CursorLine
                 \ | hi link CursorLine CursorColumn
augroup END

" Color theme
"colorscheme darkblue
"colorscheme industry
"colorscheme elflord
"colorscheme set
"colorscheme molokai
"let g:gruvbox_constrast_dark = "hard"


"""""""""""""""""""""""""""""""""""""""""""""
"           Plugin Manager (Plug)           "
"""""""""""""""""""""""""""""""""""""""""""""
"
" I also have vundle install but not configure

call plug#begin()
  " Left file tree sidebar
  Plug 'preservim/NERDTree'
  Plug 'Xuyuanp/nerdtree-git-plugin'
  Plug 'preservim/nerdcommenter'
  Plug 'jiangmiao/auto-pairs'
  Plug 'junegunn/goyo.vim'
  Plug 'frazrepo/vim-rainbow'
  Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
  Plug 'junegunn/fzf.vim'         
  Plug 'mg979/vim-visual-multi', {'branch': 'master'}

  " Use release branch (recommend)
  Plug 'neoclide/coc.nvim', {'branch': 'release'}

  " Themes
  Plug 'morhetz/gruvbox'      
  Plug 'ayu-theme/ayu-vim'

  " Plugings for plantuml
  Plug 'aklt/plantuml-syntax'
  Plug 'weirongxu/plantuml-previewer.vim'
  Plug 'tyru/open-browser.vim'

  " UNTESTED/UNCONFIGURE PLUGINGS
  "Plug 'easymotion/vim-easymotion'
  "Plug 'christoomey/vim-tmux-navigator'
call plug#end()

"colorscheme gruvbox
set termguicolors     " enable true colors support
"let ayucolor="light"  " for light version of theme
let ayucolor="mirage" " for mirage version of theme
"let ayucolor="dark"   " for dark version of theme
colorscheme ayu

"""""""""""""""""""""""""""""""""""""""""""""
"               Plugin config               "
"""""""""""""""""""""""""""""""""""""""""""""

let g:rainbow_active = 1    " Enables rainbow plugin globally


"""""""""""""""""""""""""""""""""""""""""""""
"    Mapping plugin command to keys         "
"""""""""""""""""""""""""""""""""""""""""""""
" NERDTree config
"let NERDTreeQuitOnOpen=1

noremap <leader>nt :NERDTreeToggle<cr>

"fzf config
noremap <leader>p :Files <cr>
noremap <leader>his :History <cr>
noremap <leader>H :History: <cr>

" Vim-visual-multi config
let g:VM_mouse_mappings = 1
let g:VM_maps = {}
let g:VM_maps["Undo"] = 'u'
let g:VM_maps["Redo"] = '<C-r>'
" NOTE:- NERDCommenter inject some keybinding using <leader> key and c

" TODO:- Configure this for only latex files
noremap <leader>la :w <CR>: ! sh latex/compile.sh % <cr>
noremap <leader>ls :w <CR>: ! sh latex/refcompile.sh % <cr>


"""""""""""""""""""""""""""""""""""""""""""""
"    Vim startup commands/programs          "
"""""""""""""""""""""""""""""""""""""""""""""

"autocmd VimEnter * NERDTree
" Focus new windows instead of NERDTree
"autocmd VimEnter * wincmd p            


"source $HOME/.vim/coc.vim
