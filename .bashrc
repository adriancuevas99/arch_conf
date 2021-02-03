#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return


alias cat='ccat'
alias ls='exa --group-directories-first'
alias tree='exa -T'


#alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
