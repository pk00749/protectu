package com.warcraftyork.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpSession;

@Controller
public class PoliciesController {

    @RequestMapping("/test")
    public String test(){
        return "index";
    }

    @GetMapping("/login")
    public String login(){
        return "logout.html";
    }

    @RequestMapping("/policies")
    public String policies() {
        return "policies";
    }

    @RequestMapping("/logout")
    public String logout(HttpSession session){
//        session.removeAttribute(WebSecurityConfig.SESSION_KEY);
        return "redirect:/login";
    }
}
