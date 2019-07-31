package com.warcraftyork.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpSession;

@Controller
public class PoliciesController {
    @RequestMapping("/policies")
    public String policies() {
        return "policies";
    }

    @RequestMapping("/logout")
    public String logout(HttpSession session){
//        session.removeAttribute(WebSecurityConfig.SESSION_KEY);
        return "redirect:/index";
    }
}
