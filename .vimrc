syntax on
colorscheme http__modified
"colorscheme onedark

set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'Raimondi/delimitMate'
call vundle#end()
filetype plugin indent on

let g:ycm_autoclose_preview_window_after_completion=1
let g:ycm_autoclose_preview_window_after_insertion=1
let g:ycm_key_list_select_comlpetion=['<Enter>', '<Down>']
let g:ycm_key_list_select_comlpetion=['<Up>']
let g:ycm_key_list_stop_completion=['<Enter>']
let g:ycm_min_num_of_chars_for_completion=2
let g:ycm_seed_identifiers_with_syntax=1
let g:ycm_python_binary_path='python'
let g:ycm_max_num_candidates=7
let g:ycm_max_num_identifier_candidates=7
let g:ycm_complete_in_comments=1
let g:ycm_complete_in_strings=1
let g:ycm_collect_identifiers_from_comments_and_strings=1
inoremap <expr> <CR> pumvisible() ? "\<C-y>" : "\<CR>"
map <leader> g:YcmCompleter GoToDefinitionElseDeclaration<CR>

set tabstop=4
set nu
set ic
set mouse=a
set hlsearch
set encoding=utf-8
set fileencodings=utf-8,ucs-bom,GB2312,big5
set cursorline
set autoindent
set smartindent
set vb
set scrolloff=4
set showmatch

nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

let python_hight_all=1
au Filetype python set tabstop=4
au Filetype python set softtabstop=4
au Filetype python set shiftwidth=4
au Filetype python set expandtab
au Filetype python set autoindent
au Filetype python set fileformat=unix
autocmd Filetype python set foldmethod=indent
autocmd Filetype python set foldlevel=99

map <F5> :call CompileRunGcc()<CR>
func! CompileRunGcc()
		exec "W"
		if &filetype == 'python'
				exec "!time python3 %"
		endif
endfunct
