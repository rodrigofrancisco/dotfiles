" ConfiguraciOn general {
    " ConfiguraciOn vim
    set nocompatible
    filetype off

    " ConfiguraciOn texto y navegaciOn
    set number
    set relativenumber " NumeraciOn de lIneas desde tu posiciOn actual
    set linebreak
    set showbreak=...\              " Se muestran 3 puntos para simbolizar continuaciOn
    if has("patch-7.4.354") || has('nvim')
        set breakindent
    endif
    set textwidth=100
    set showmatch
    "set matchpairs+=¡:!
    set visualbell
    set ruler

    " ConfiguraciOn para la busqueda
    set hlsearch
    set smartcase
    set ignorecase
    set incsearch

    " Ex menU
    "set path+=**       " BUsqueda recursiva de archivos
    set wildmenu        " Se pueden visualizar las opciones con tab

    " ConfiguraciOn para el indentado automAtico
    set autoindent
    set smarttab
    set tabstop=4
    set softtabstop=4
    set shiftwidth=4
    set expandtab

    " RepresentaciOn de los carActeres invisibles
    "set list
    "set listchars=tab:▸\ ,trail:⋅,extends:❯,precedes:❮

    " Guias visuales, se resalta la lInea y columna actuales y la columna 80
    set cursorline
    set cursorcolumn
    set colorcolumn=80

    " Extras
    "set autowrite
    "set spelllang=es
    "set spell
    "set undolevels=1000
    "set backspace=indent,eol,start
    "set splitright
    "set splitbelow
    "set nrformats+=alpha
    if has('conceal')
        set concealcursor=
    endif
" }

" Mapeos {

    " Mapeos bAsicos
    let mapleader = "\,"
    nnoremap Q <nop>
    inoremap kj <Esc>
    nnoremap <C-k> -l
    nnoremap <C-j> +l
    nnoremap <space> za
    nnoremap Y y$
    nmap <leader>ff zfaf
    nnoremap <leader>cbox :Tabularize /*<cr>vip<Esc>:substitute/ /=/g<cr>r A/<Esc>vipo<Esc>0r/:substitute/ /=/g<cr>:nohlsearch<cr>
    nnoremap <leader>r :%s/\<<C-r>=expand("<cword>")<CR>\>\C//g<Left><Left>
    nnoremap <leader>R :%s/\<<C-r>=expand("<cWORD>")<CR>\>\C//g<Left><Left>
    inoremap <leader>pk <Esc>:VCoolor<Return>a
    inoremap <leader>scp <Esc>:!gpick<Return>a

    " Para modificar fácilmente este archivo
    nnoremap <leader>av :tabnew $MYVIMRC<CR>
    nnoremap <leader>sv :source $MYVIMRC<CR>

    " Abreviaciones
    iabbrev fro for
    iabbrev lenght length
    iabbrev widht  width
    iabbrev heigth height
    iabbrev prt    ptr
    iabbrev tis    this
    iabbrev tihs   this
    iabbrev form   from

    " Manejo de ventanas
    nnoremap \| :vsplit<space>
    nnoremap _ :split<space>

    " Manejo de tabulaciones
    nnoremap <leader>tn :tabnew<Space>

    nnoremap <leader>tk :tabnext<CR>
    nnoremap <leader>tj :tabprev<CR>
    nnoremap <leader>th :tabfirst<CR>
    nnoremap <leader>tl :tablast<CR>

    " Mapeos del modo comando {
        " Movimiento estilo emacs
        cnoremap <C-a> <Home>
        cnoremap <C-b> <Left>
        cnoremap <C-f> <Right>
        cnoremap <C-d> <Delete>
        cnoremap <M-b> <S-left>
        cnoremap <M-f> <S-right>
        cnoremap <M-d> <S-right><C-w>

        " Escribir archivos que requieren sudo
        cnoremap w!! w !sudo tee % >/dev/null
        " Evitar el uso errOneo de mayUsculas
        " al intentar salir o guardar un archivo
        cnoremap Q q
        cnoremap W w
        cnoremap WW W
        cnoremap QQ Q
    " }
