# browser_history_project# Browser History Simulator (DSA Project)

## Overview
Simulates browser navigation using two stacks.

## Data Structures Used
- Stack (Python list)
- Back stack and forward stack

## Features
- Visit a page
- Go back
- Go forward
- View current page

## How It Works
- Visiting a new page clears forward history
- Back moves current page to forward stack
- Forward moves current page to back stack

## Example
visit google → youtube → leetcode  
back → youtube  
back → google  
forward → youtube